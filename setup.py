import os
import sys

def setup():
    os.system("mv main.py /usr/bin/runas.py")
    os.system("mv launch.sh /usr/bin/runas");
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