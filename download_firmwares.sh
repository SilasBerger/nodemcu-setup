#!/bin/bash

firmwares=(
"https://micropython.org/resources/firmware/ESP32_GENERIC_C3-20240222-v1.22.2.bin"
)

if [ ! -d firmware ]; then
    mkdir firmware
fi

for firmware in $firmwares; do
  (cd ./firmware && curl -O $firmware)
done