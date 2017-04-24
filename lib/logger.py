#
# Imports
#

import logging

#
# Description: Enable route hit logging with class, function and line numbers
#

logging_format = "[%(asctime)s] %(process)d-%(levelname)s "
logging_format += "%(module)s::%(funcName)s():l%(lineno)d: "
logging_format += "%(message)s"

logging.basicConfig(
  format=logging_format,
  level=logging.DEBUG
)

log = logging.getLogger()