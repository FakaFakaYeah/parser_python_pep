import logging

from requests import RequestException

from exceptions import ParserFindTagException, StringFindException


def get_response(session, url):
    try:
        response = session.get(url) 
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag, attrs=None, method='find'):
    try:
        searched_tag = getattr(soup, method)(tag, attrs=(attrs or {}))
    except AttributeError:
        error_msg = f'У объекта soup нет метода {method}'
        logging.error(error_msg)
        raise AttributeError(error_msg)
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def find_string(soup, string):
    searched_string = soup.find(string=string)
    if searched_string is None:
        error_msg = f'Не найден строка: {string}'
        logging.error(error_msg, stack_info=True)
        raise StringFindException(error_msg)
    return searched_string
