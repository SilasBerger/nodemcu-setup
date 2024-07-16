# NodeMCU Setup
Setup instructions, scripts and helper files for ESP32 NodeMCU development boards.

## Initial setup
For the initial setup, run the following commands from the root of this repository:
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
| 3   | SX1267 ESP32 LoRa                                                                                                       | ESP32    | https://micropython.org/download/ESP32_GENERIC/      <br/>| https://de.aliexpress.com/item/1005005967763162.html  |

## Flashing firmware
Determine the appropriate setup script for your chip / board. Use the above board inventory for assistance.

Next, plugin in the ESP32 device. **Make sure to only plug in the device you wish to flash!**.

Then Execute the appropriate setup script (e.g. `setup_scripts/esp32_c3_v1.22.2.sh`) from the **repository root**.

```shell
setup_scripts/esp32_c3_v1.22.2.sh
```

## Serial connections: REPL and file transfer
### REPL / Shell
You can connect your shell to the Micropython environment by using serial I/O command-line tool such as [tio](https://github.com/tio/tio) (recommended, manual installation required) or the PySerial Miniterm (provided in this project's virtualenv).

To establish a serial connection, you first need to determine which serial port to use. The easiest way to accomplish this is to run

```shell
./esptool.py chip_id | grep "Serial port"
```

Then, run

```shell
tio <serial_port>
```

to connect to the device. 

If you prefer using the provided PySerial Minitern, run

```shell
python -m serial.tools.miniterm <serial_port>
```

instead.

Once the serial connection is established, you have access to the Python REPL on the ESP32 Micropython device.

Run

```python
print("Hello, world!")
```

to verify that everything is working correctly. You can also execute Python files on the device (see [Working with files](#working-with-files)) by running

```python
import some_file
```

### Working with files
File management is handled through the `ampy` Python module.

First, determine the serial port to be used by running

```shell
./esptool.py chip_id | grep "Serial port"
```

Then, you can use the following file management commands:
- **Upload a file:** `./ampy.py -p <serial_port> put demos/hello_world.py main.py`. This uploads a local file `demos/hello_world.py` to the device's flash memory root and names it `main.py`.
- **List files:** `./ampy.py -p <serial_port> ls`. This lists all files in the device's flash memory.
- **See all commands:** `./ampy --help`

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

**Note:** Some demos may be specific to a particular development board; especially with respect to the pin layout.
