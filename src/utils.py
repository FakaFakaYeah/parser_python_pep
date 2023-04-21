import logging

from requests import RequestException

from exceptions import ParserFindTagException


def get_response(session, url):
    """Метод проверки подключения к странице"""
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag=None, attrs=None, string=None, method='find'):
    """Метод поиска тега, по-умолчанию метод find"""
    try:
        searched_tag = getattr(soup, method)(
            tag, attrs=(attrs or {}), string=string or ''
        )
    except AttributeError as error:
        error_msg = f'Тэг не найден: {error}'
        logging.error(error_msg)
        raise AttributeError(error_msg)
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs} {string}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag
