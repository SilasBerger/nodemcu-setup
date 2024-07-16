#!/bin/bash
source venv/bin/activate
./esptool.py erase_flash
./esptool.py write_flash -z 0x1000 ./firmware/ESP32_GENERIC-20240602-v1.23.0.bin
