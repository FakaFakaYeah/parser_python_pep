from requests import RequestException

from exceptions import ParserFindTagException, RequestError


def get_response(session, url):
    """Метод проверки подключения к странице"""
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        raise RequestError(f'Возникла ошибка при загрузке страницы {url}')


def find_tag(soup, tag=None, attrs=None, string=None, method='find'):
    """Метод поиска тега, по-умолчанию метод find"""
    try:
        searched_tag = getattr(soup, method)(
            tag, attrs=(attrs or {}), string=string or ''
        )
    except AttributeError as error:
        raise AttributeError(f'Тэг не найден: {error}')
    if searched_tag is None:
        raise ParserFindTagException(f'Не найден тег {tag} {attrs} {string}')
    return searched_tag
