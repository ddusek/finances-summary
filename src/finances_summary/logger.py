import logging
from datetime import date
from finances_summary.settings import ROOT_DIR

# Logging.
logging.basicConfig(
    filename=f'{ROOT_DIR}/logs/{date.today().isoformat()}.log',
    filemode='a+',
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%H:%M:%S',
)
LOGGER = logging.getLogger(__name__)


def except_handler(type, value, tb):
    LOGGER.exception('Uncaught exception: %s', str(value))
