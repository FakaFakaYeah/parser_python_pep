class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class RequestError(Exception):
    """Вызывается, когда парсер не смог подключится по нужному адресу"""
    pass
