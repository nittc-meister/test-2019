import subprocess
import sys
try:
    res = subprocess.check_output("python ./hello-world.py")
except:
    print("処理に失敗しました")
    sys.exit(1)

print(res)
if (res != "Hello World!"):
    print("出力された文字列が一致しません: " + res)
    sys.exit(1)
