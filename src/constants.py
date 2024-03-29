from pathlib import Path

MAIN_DOC_URL = 'https://docs.python.org/3/'
BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOG_FORMAT = (
    '"%(asctime)s - [%(levelname)s] - %(message)s - '
    'Имя функции:[%(funcName)s] - %(lineno)d"'
)
LOG_DT_FORMAT = '%d.%m.%Y %H:%M:%S'
PEP_URL = 'https://peps.python.org/'
EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}
PRETTY = 'pretty'
FILE = 'file'
DOWNLOADS_DIR = 'downloads'
RESULTS_DIR = 'results'
LOGS_DIR = 'logs'
