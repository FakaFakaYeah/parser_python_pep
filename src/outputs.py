import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import BASE_DIR, DATETIME_FORMAT, PRETTY, FILE, RESULTS_DIR


def control_output(results, cli_args):
    """Конфигуратор вывода результата"""
    output = cli_args.output
    if output == PRETTY:
        pretty_output(results)
    elif output == FILE:
        file_output(results, cli_args)
    else:
        default_output(results)


def default_output(results):
    """Обычный вывод в терминал"""
    for row in results:
        print(*row)


def pretty_output(results):
    """Вывод результата в таблицу"""
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)


def file_output(results, cli_args):
    """Вывод результата в csv файл"""
    results_dir = BASE_DIR / RESULTS_DIR
    results_dir.mkdir(exist_ok=True)
    now = dt.datetime.now()
    file_name = f'{cli_args.mode}_{now.strftime(DATETIME_FORMAT)}.csv'
    file_path = results_dir / file_name

    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, dialect='unix')
        writer.writerows(results)
    logging.info(f'Файл с результатами был сохранён: {file_path}')
