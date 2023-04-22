import logging
import re
from urllib.parse import urljoin

import requests_cache
from bs4 import BeautifulSoup
from tqdm import tqdm

from configs import configure_argument_parser, configure_logging
from constants import (
    BASE_DIR, MAIN_DOC_URL, PEP_URL, EXPECTED_STATUS, DOWNLOADS_DIR
)
from outputs import control_output
from utils import get_response, find_tag


def whats_new(session):
    """Парсер нововведений версий Python"""
    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')

    soup = BeautifulSoup(
        get_response(session, whats_new_url).text, features='lxml'
    )
    div_with_ul = find_tag(
        find_tag(soup, 'section', attrs={'id': 'what-s-new-in-python'}),
        'div', attrs={'class': 'toctree-wrapper'}
    )
    sections_by_python = div_with_ul.find_all('li',
                                              attrs={'class': 'toctree-l1'})

    results = [('Ссылка на статью', 'Заголовок', 'Редактор, Автор')]
    for section in tqdm(sections_by_python, desc='Идет сбор информации!'):
        version = find_tag(section, 'a')
        version_link = urljoin(whats_new_url, version['href'])

        soup = BeautifulSoup(
            get_response(session, version_link).text, features='lxml'
        )
        h1 = find_tag(soup, 'h1')
        dl = find_tag(soup, 'dl')
        dl_text = dl.text.replace('\n', ' ')
        results.append((version_link, h1.text, dl_text))

    return results


def latest_versions(session):
    """Парсер сбора информации о версиях Python"""
    soup = BeautifulSoup(
        get_response(session, MAIN_DOC_URL).text, features='lxml'
    )
    sidebar = find_tag(soup, 'div', attrs={'class': 'sphinxsidebarwrapper'})
    ul_tags = sidebar.find_all('ul')

    for ul in tqdm(ul_tags, desc='Идет сбор информации!'):
        if 'All version' in ul.text:
            a_tags = ul.find_all('a')
            break
        else:
            raise Exception('Ничего не нашлось')

    results = [('Ссылка на статью', 'Заголовок', 'Редактор, Автор')]
    pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'

    for a_tag in tqdm(a_tags):
        link = a_tag['href']
        text_match = re.search(pattern, a_tag.text)
        if text_match is not None:
            version, status = text_match.groups()
        else:
            version, status = a_tag.text, ''
        results.append((link, version, status))
    return results


def download(session):
    """Парсер скачивания архива с документацией Python"""
    downloads_url = urljoin(MAIN_DOC_URL, 'download.html')

    soup = BeautifulSoup(
        get_response(session, downloads_url).text, features='lxml'
    )
    pdf_a4_link = find_tag(
        find_tag(soup, 'table', attrs={'class': 'docutils'}), 'a',
        attrs={'href': re.compile(r'.+pdf-a4\.zip$')}
    )['href']
    archive_url = urljoin(downloads_url, pdf_a4_link)

    filename = archive_url.split('/')[-1]
    downloads_dir = BASE_DIR / DOWNLOADS_DIR
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename

    response = get_response(session, archive_url)
    with open(archive_path, 'wb') as file:
        file.write(response.content)
    logging.info(f'Архив был загружен и сохранён: {archive_path}')


def pep(session):
    """Парсер сбора статистики о документах PEP"""
    soup = BeautifulSoup(get_response(session, PEP_URL).text, features='lxml')
    section = find_tag(soup, 'section', attrs={'id': 'index-by-category'})
    pep_list = section.find_all(
        'table', class_='pep-zero-table docutils align-default'
    )

    status_count = {}
    results = [('Статус', 'Количество')]
    for pep_block in tqdm(pep_list, desc='Обработано блоков PEP'):
        pep_group = find_tag(pep_block, 'tbody').find_all('tr')

        for pep in pep_group:
            type_status = find_tag(pep, 'td').text
            preview_status = type_status[1:]
            pep_page = urljoin(
                PEP_URL,
                find_tag(
                    pep, 'a', attrs={'class': 'pep reference internal'}
                )['href']
            )

            soup = BeautifulSoup(
                get_response(session, pep_page).text, features='lxml'
            )
            status = find_tag(
                find_tag(
                    find_tag(
                        soup, 'dl',
                        attrs={'class': 'rfc2822 field-list simple'}
                    ),
                    string='Status'
                ).parent,
                'dd', method='find_next_sibling'
            ).text

            if status not in EXPECTED_STATUS[preview_status]:
                logging.info(f"""
                Статус на странице {pep_page}
                не совпадает со статусом на странице {PEP_URL}.
                Cтатус в карточке: {status}
                Ожидаемы статусы {EXPECTED_STATUS[preview_status]}
                """)
            status_count.setdefault(status, 0)
            status_count[status] += 1
    total = sum(status_count.values())
    results += tuple(status_count.items())
    results.append(('Total', total))
    return results


MODE_TO_FUNCTION = {
    'whats-new': whats_new,
    'latest-versions': latest_versions,
    'download': download,
    'pep': pep,
}


def main():
    try:
        configure_logging()
        logging.info('Парсер запущен!')

        parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
        args = parser.parse_args()
        logging.info(f'Аргументы командной строки: {args}')

        session = requests_cache.CachedSession()
        if args.clear_cache:
            session.cache.clear()
        results = MODE_TO_FUNCTION[args.mode](session)

        if results is not None:
            control_output(results, args)
        logging.info('Парсер завершил работу.')
    except Exception as error:
        logging.error(
            f"Сбой в работе программы: {error}",
            stack_info=True
        )


if __name__ == '__main__':
    main()
