# NodeMCU Setup
Setup instructions, scripts and helper files for ESP32 NodeMCU development boards.

## Initial setup
- `pip3 -m venv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`
- `python esptool.py --help`
- `chmod +x ./download_firmwares.sh && ./download_firmwares.sh`
- `chmod +x setup_scripts/*`

## Board inventory for Micropython firmware
_For diagrams (such as pinout, etc.), see `diagrams/device_<deviceNr>`._

| Nr. | Name                                                                                                                    | SoC      | Micropython Firmware                                 | Link                                                  |
|-----|-------------------------------------------------------------------------------------------------------------------------|----------|------------------------------------------------------|-------------------------------------------------------|
| 1   | ESP32 C3 / RP2040 Raspberry Pi Pico Development Board With 0.42 Inch LCD Risc-v WiFi Bluetooth for Arduino Microprython | ESP32 C3 | https://micropython.org/download/ESP32_GENERIC_C3/   | https://www.aliexpress.com/item/1005006051061995.html |
| 2   | LILYGO TTGO LORA32                                                                                                      | ESP32    | https://micropython.org/download/LILYGO_TTGO_LORA32/ | https://www.aliexpress.com/item/1005003088139358.html |

## Flashing firmware
First, you need to determine the correct USB device on which the ESP32 is connected. Run this command as a starting point:
```shell
ls /dev | grep usb
```

Then, you need to run the appropriate setup script (e.g. `setup_scripts/esp32_c3_v1.22.2.sh`) with the `USB_DEV` environment variable set to the device value from the previous step. **Note:** this command needs to be run from the repository root!

```shell
USB_DEV=tty.usbmodem1101 setup_scripts/esp32_c3_v1.22.2.sh
```

## REPL
Make sure the `picocom` command line utility is installed, e.g.: `brew install picocom`. 

Then, connect to the ESP32 device as follows: `picocom -b 115200 /dev/tty.usbmodem1101` (replace `tty.usbmodem1101` with the appropriate USB device if needed).

Now you are in the Micropython REPL.

## Working with files
List files on device:
```shell
./ampy.py -p /dev/tty.usbmodem1101 ls
```

Upload a `main.py` file:
```shell
./ampy.py -p /dev/tty.usbmodem1101 ls
```

_Note that the variables defined in this script will also be available globally in the REPL._

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
