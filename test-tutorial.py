import subprocess
import sys
try:
    res = subprocess.check_output("python ./hello-world.py")
except:
    sys.exit(1)

if (res != "Hello World!"):
    sys.exit(1)
