import logging.config
from pathlib import Path


def configure_logging() -> None:
    path = Path(__file__).with_name('logging.conf')
    logging.config.fileConfig(path)
    log = logging.getLogger(__name__)
    log.debug('Logging is configured.')


INPUT_FEED_URL = 'https://www.kdnuggets.com/feed'
