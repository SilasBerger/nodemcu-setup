# NodeMCU Setup
Setup instructions, scripts and helper files for ESP32 NodeMCU development boards.

## Initial setup
- `pip3 -m venv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`
- `python esptool.py --help`
- `chmod +x ./download_firmwares.sh && ./download_firmwares.sh`
- `chmod +x setup_scripts/* command_generator.sh`

## Board inventory for Micropython firmware
_For diagrams (such as pinout, etc.), see `diagrams/device_<deviceNr>`._

| Nr. | Name                                                                                                                    | SoC      | Micropython Firmware                                 | Link                                                  |
|-----|-------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------|-------------------------------------------------------|
| 1   | ESP32 C3 / RP2040 Raspberry Pi Pico Development Board With 0.42 Inch LCD Risc-v WiFi Bluetooth for Arduino Microprython | ESP32 C3 | https://micropython.org/download/ESP32_GENERIC_C3/   | https://www.aliexpress.com/item/1005006051061995.html |
| 2   | LILYGO TTGO LORA32                                                                                                      | ESP32    | https://micropython.org/download/LILYGO_TTGO_LORA32/ | https://www.aliexpress.com/item/1005003088139358.html |

## Flashing firmware
Determine the appropriate setup script for your chip / board. Use the above board inventory for assistance.

Then Execute the appropriate setup script (e.g. `setup_scripts/esp32_c3_v1.22.2.sh`) from the **repository root**.

```shell
setup_scripts/esp32_c3_v1.22.2.sh
```

## Serial connections: REPL and file transfer
Run 

```shell
./command-generator.py
```

to get a list of useful commands for connecting to the device's REPL or transferring files, tailored to the serial port that your device is most likely connected to. Use and customize these commands as you see fit.

Here are some usage examples where the port happens to be `/dev/tty.usbmodem1101`:
- Entering a Micropython REPL: `python -m serial.tools.miniterm /dev/tty.usbmodem1101`
- List all files in the device's flash memory: `./ampy.py -p /dev/tty.usbmodem1101 ls`
- Upload a `main.py` file: `./ampy.py -p /dev/tty.usbmodem1101 demos/hello_world.py main.py`

## ESP32 Micropython essentials
For more, see https://docs.micropython.org/en/latest/esp32/quickref.html.

### Networks
```python
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.scan()
```

### GPIO output
```python
from machine import Pin
pin8 = Pin(8, Pin.OUT)
pin8.on()
```

## Demo files
The `demos` directory contains some demo scripts that can be uploaded to the device (see [Working with files](#working-with-files)).

**Note:** Some demos may be specific to a particular devleopment board; especially with respect to the pin layout.
