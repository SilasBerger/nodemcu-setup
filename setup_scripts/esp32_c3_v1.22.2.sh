#!/bin/bash
pwd
source venv/bin/activate
./esptool.py --chip esp32c3 --port /dev/$USB_DEV erase_flash
./esptool.py --chip esp32c3 --port /dev/$USB_DEV --baud 460800 write_flash -z 0x0 ./firmware/ESP32_GENERIC_C3-20240222-v1.22.2.bin
