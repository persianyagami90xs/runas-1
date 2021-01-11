import os
import sys

def setup():
    os.system("cp main.py /usr/bin/runas.py")
    os.system("cp launch.sh /usr/bin/runas");
    os.system("chmod +x /usr/bin/runas");

def uninstall():
    os.system("rm -rf /usr/bin/runas.py")
    os.system("rm -rf /usr/bin/runas")

if __name__ == "__main__":
    if sys.argv[1] == "install":
        setup()

    elif sys.argv[1] == "uninstall":
        uninstall()

    else:
        sys.exit(1)