#!/bin/bash
pwd
source venv/bin/activate
./esptool.py erase_flash
./esptool.py write_flash -z 0x0 ./firmware/ESP32_GENERIC_C3-20240222-v1.22.2.bin
