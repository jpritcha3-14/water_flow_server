# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import math
import time
import sqlite3
import atexit

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0


# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
#disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Initialize library.
disp.begin()

# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))

# Load default font.
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 15)
# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as this python script!
# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

# Create drawing object.
draw = ImageDraw.Draw(image)

# Animate text moving in sine wave.
print('Press Ctrl-C to quit.')
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def closeAndClear(conn=conn, draw=draw):
    conn.close()
    draw.rectangle((0,0,width,height), outline=0, fill=0)

atexit.register(closeAndClear, conn)

def drawLine(x, y, text):
    for ch in text:
        # Stop drawing if off the right side of screen.
        if x > width:
            return
        # Draw text.
        draw.text((x, y), ch, font=font, fill=255)
        # Increment x position based on chacacter width.
        char_width, char_height = draw.textsize(ch, font=font)
        x += char_width

while True:
    # Clear image buffer by drawing a black filled box.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Enumerate characters and draw them offset vertically based on a sine wave.
     
    with conn:
        c.execute('SELECT val FROM display_flow_flow WHERE timestamp = (SELECT MAX(timestamp) FROM display_flow_flow);')
        count = c.fetchall()[0][0]

    drawLine(0,0,'Flow Rate:') 
    drawLine(0,15,str(count) + ' L/Min') 
    drawLine(0,30,'Max Flow Rate:') 
    drawLine(0,45,'Placeholder') 
    
    # Draw the image buffer.
    disp.image(image)
    disp.display()
    count += 1
    # Pause briefly before drawing next frame.
    time.sleep(2)


