import os
import sys

def main(argc: int, argv: list):
    command = ""

    argv.pop(0)

    tokens = argv

    for token in tokens:
        if command == "":
            command = command + token

        else:
            command = command + " " + token

    os.system("su root -c \"" + command + "\"")

if __name__ == "__main__":
    main(argc=len(sys.argv), argv=sys.argv)
