from util import resource_path

import sys
import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter("%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s")

log_file = resource_path("log.txt")

rotating_file_handler = RotatingFileHandler(log_file, mode="a", maxBytes=1024*1024, backupCount=1)
rotating_file_handler.setFormatter(log_formatter)
rotating_file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_formatter)

logger = logging.getLogger('root')
logger.setLevel(logging.INFO)
logger.addHandler(rotating_file_handler)
logger.addHandler(console_handler)
