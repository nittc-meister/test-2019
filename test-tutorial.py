import subprocess
import sys
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

if (res != "Hello World!\n"):

    logger.error("出力された文字列が一致しません: " + repr(res))
    sys.exit(1)
