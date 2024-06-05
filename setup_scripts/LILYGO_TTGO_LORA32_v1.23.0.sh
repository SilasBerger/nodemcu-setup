#!/bin/bash
pwd
source venv/bin/activate
./esptool.py erase_flash
./esptool.py write_flash -z 0x1000 ./firmware/LILYGO_TTGO_LORA32-20240602-v1.23.0.bin
