import subprocess

from cli.util import determine_unique_port_or_fail, determine_baud_rate


def main():
    port = determine_unique_port_or_fail()
    print("- shell:", "python -m serial.tools.miniterm", port)
    print("- file transfer: ./ampy.py -p", port, "put path/to/file.py main.py")


if __name__ == "__main__":
    main()
