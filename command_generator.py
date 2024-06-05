#!python

from cli.util import determine_unique_port_or_fail


def main():
    port = determine_unique_port_or_fail()
    print("SHELL:", "python -m serial.tools.miniterm", port)
    print("FILE TRANSFER: ./ampy.py -p", port, "put path/to/file.py main.py")


if __name__ == "__main__":
    main()
