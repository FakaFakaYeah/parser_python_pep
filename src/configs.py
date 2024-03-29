import argparse
import logging
from logging.handlers import RotatingFileHandler

from constants import (
    BASE_DIR, LOG_FORMAT, LOG_DT_FORMAT, FILE, PRETTY, LOGS_DIR
)


def configure_argument_parser(available_modes):
    """Конфигуратор парсера"""
    parser = argparse.ArgumentParser(description='Парсер документации Python')

    parser.add_argument(
        'mode',
        choices=available_modes,
        help='Режимы работы парсера'
    )

    parser.add_argument(
        '-c',
        '--clear-cache',
        action='store_true',
        help='Очистка кеша'
    )

    parser.add_argument(
        '-o',
        '--output',
        choices=(PRETTY, FILE),
        help='Дополнительные способы вывода данных'
    )

    return parser


def configure_logging():
    """Конфигурато логов"""
    log_dir = BASE_DIR / LOGS_DIR
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'parser.log'

    roating_hendler = RotatingFileHandler(
        log_file, maxBytes=10 ** 6, backupCount=5, encoding='utf-8'
    )

    logging.basicConfig(
        datefmt=LOG_DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(roating_hendler, logging.StreamHandler())
    )
