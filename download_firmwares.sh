#!/bin/bash

firmwares=(
"https://micropython.org/resources/firmware/ESP32_GENERIC_C3-20240222-v1.22.2.bin"
"https://micropython.org/resources/firmware/LILYGO_TTGO_LORA32-20240602-v1.23.0.bin"
"https://micropython.org/resources/firmware/ESP32_GENERIC-20240602-v1.23.0.bin"
)

if [ ! -d firmware ]; then
    mkdir firmware
fi

for firmware in ${firmwares[@]}; do
  (cd ./firmware && curl -O $firmware)
done
