import subprocess
import sys
import re
from logging import basicConfig, getLogger, DEBUG
basicConfig(level=DEBUG)
logger = getLogger(__name__)
logger.debug('hello')

try:
    res = subprocess.check_output(["python",
                                   "./hello-world.py"]).decode("utf-8")
except:
    logger.error("処理に失敗しました")
    sys.exit(1)

logger.debug(repr(res))

if re.match(res, r"^Hello World! s\d{5}\n$"):

    logger.error("出力された文字列が一致しません: " + repr(res))
    sys.exit(1)
