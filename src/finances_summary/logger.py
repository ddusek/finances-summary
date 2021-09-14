import logging
from datetime import date
from finances_summary.settings import ROOT_DIR


# Logging.
logging.basicConfig(
    filename=f"{ROOT_DIR}/logs/{date.today().isoformat()}.log",
    filemode="a+",
    encoding="utf-8",
    level=logging.WARNING,
)
LOGGER = logging.getLogger(__name__)
