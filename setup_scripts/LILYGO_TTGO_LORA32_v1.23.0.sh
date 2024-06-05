#!/bin/bash
pwd
source venv/bin/activate
./esptool.py --chip esp32 --port /dev/$USB_DEV erase_flash
./esptool.py --chip esp32 --port /dev/$USB_DEV --baud 460800 write_flash -z 0x0 ./firmware/LILYGO_TTGO_LORA32-20240602-v1.23.0.bin
