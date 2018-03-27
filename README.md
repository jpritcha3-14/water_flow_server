# Water flow project to measure and record water flow data for agricultural applications in Python 3

## Hardware Bill of Materials
* Raspberry Pi model 3 Ver. B ([Amazon](https://www.amazon.com/gp/product/B01CD5VC92/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1))
* Prototype Hat shield for Raspberry Pi ([Amazon](https://www.amazon.com/gp/product/B01G8DPGWY/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1))
* Bi-Directional Logic Level Converter ([Sparkfun](https://www.sparkfun.com/products/12009))
* I2C OLED Module 12864 ([Amazon](https://www.amazon.com/gp/product/B00O2LLT30/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1))
* YF-S201 1-30L/min Hall Effect Water Flow Meter ([Amazon](https://www.amazon.com/YF-S201-Counter-Sensor-control-Flowmeter/dp/B073W7T8BZ/ref=sr_1_1?s=industrial&ie=UTF8&qid=1522120633&sr=1-1&keywords=yf-s201))
* Male Pin Headers
* Patch Wire
* Solder

## Wiring Setup
### (Box = Component, Circle = Connection Point)

```mermaid
graph LR
    RPi(RPi) -- GPIO --- RPi_Hat(Rpi Hat)
```
```mermaid
graph LR
    RPi_Hat(RPi Hat) --- 3.3V((3.3V))
    RPi_Hat --- 5V((5V))
    RPi_Hat --- 18((18))
    RPi_Hat --- 23((23))
    5V --- HV((HV))
    3.3V --- LV((LV))
    HV --- level_shifter(Level Shifter)
    LV --- level_shifter
    18 --- LV1((LV1))
    23 --- LV2((LV2))
    LV1 --- level_shifter
    LV2 --- level_shifter 
```
```mermaid
graph LR
    level_shifter(Level Shifter) --- HV1((HV1/2))
    HV1 --- yellow1((Yellow))
    yellow1 --- flow1(Flow Sensor 1/2)
    RPi_Hat(RPi Hat) --- gnd((GND))
    RPi_Hat --- 5V((5V))
    gnd --- black1((Black))
    5V --- red1((Red))
    black1 --- flow1
    red1 --- flow1
```
```mermaid
graph LR
    RPi_Hat(RPi Hat) --- 3.3V((3.3V))
    RPi_Hat --- SCL1((SCL))
    RPi_Hat --- SDA1((SDA))
    RPi_Hat --- GND1((GND))
 
    3.3V --- VCC((VCC))
    VCC --- OLED(OLED)
    SCL1 --- SCL2((SCL))
    SDA1 --- SDA2((SDA))
    SCL2 --- OLED
    SDA2 --- OLED
    GND1 --- GND2((GND))
    GND2 --- OLED
```

## Completed Hardware Setup

![alt text](https://raw.githubusercontent.com/jpritcha3-14/water_flow_server/master/images/complete_setup.jpg "Completed Hardware Setup")

## Software Libraries Utilized
* [django](https://www.djangoproject.com/) - Web interface and ORM for database
* [wiringpi](http://wiringpi.com/) (more specifically the [Python wrapper](https://github.com/WiringPi/WiringPi-Python)) - Capture data from the flow sensor via GPIO
* [Adafruid_SSD1306](https://pypi.python.org/pypi/Adafruit-SSD1306) - Control OLED display via I2C.

## Running The Program

* Before starting up the flow server for the first time, navigate to the flow_server directory and run :
    ```bash
    $ python3 manage.py migrate
    ```
    This will initialize the sqlite3 database.   It only needs to be run once.
* Using your favorite text editor, edit line 4 of flow_server/spinUp.py to match  the ip address of your RPi.
* To start the program, ensure you are still in the flow_server directory and run:
    ```bash
    $ python3 spinUp.py
    ```
## Example Server Response
http://[ip_address]:[port]/display_flow/hour/

![alt text](https://raw.githubusercontent.com/jpritcha3-14/water_flow_server/master/images/flow_past_hour.jpg "Server Response Example")
