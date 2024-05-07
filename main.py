#  General
## Gather the noise level, date, put it into a .csv file and save it.

#  MicroSD Module,
## Set up for usage


#  Microphone Module
## Set up for usage
import machine
import time
from machine import I2S
from machine import Pin
import uctypes

# Configuration

SCK_PIN = machine.Pin(18) # Serial Clock connected to GP
WS_PIN = machine.Pin(19) # World Clock connected to GP12
SD_PIN = machine.Pin(20) # Serial Data connected to GP11
audio_in = I2S(0, sck=SCK_PIN, ws=WS_PIN, sd=SD_PIN, mode=I2S.RX,
               bits=32, format=I2S.STEREO,rate=16000, ibuf=20000)
samples = bytearray(2048)

while True:
    time.sleep(0.1)
    num_bytes_read = audio_in.readinto(samples)
    print(num_bytes_read)


#  General
## Gather the noise level, date, put it into a .csv file and save it.

#  MicroSD Module,
## Set up for usage


#  Microphone Module
## Set up for usage
import machine
import time
from machine import I2S
from machine import Pin
import uctypes

# Configuration

SCK_PIN = machine.Pin(18, Pin.IN) # Serial Clock connected to GP
WS_PIN = machine.Pin(19, Pin.IN) # World Clock connected to GP12
SD_PIN = machine.Pin(20, Pin.IN) # Serial Data connected to GP11
audio_in = I2S(0, sck=SCK_PIN, ws=WS_PIN, sd=SD_PIN, mode=I2S.RX,
               bits=32, format=I2S.STEREO,rate=16000, ibuf=20000)
samples = bytearray(2048)

while True:
    time.sleep(0.1)
    


#  Clock Module
## Tell time
from machine import I2C, Pin
from urtc import DS1307
import utime
from time import sleep

i2c = I2C(0,scl = Pin(1),sda = Pin(0),freq = 400000)
rtc = DS1307(i2c)

def show_time(wait):
    (year,month,date,day,hour,minute,second,p1)=rtc.datetime()
    utime.sleep(wait)
    print(rtc.datetime())
    

def set_time():
    year = int(input("Year : "))
    month = int(input("month (Jan --> 1 , Dec --> 12): "))
    date = int(input("date : "))
    day = int(input("day (1 --> monday , 2 --> Tuesday ... 0 --> Sunday): "))
    hour = int(input("hour (24 Hour format): "))
    minute = int(input("minute : "))
    second = int(input("second : "))
    now = (year,month,date,day,hour,minute,second,0)
    rtc.datetime(now)


#  RGB LED
## Use the on board RGB led as a debugging tool and as a volume warning
"""
from machine import Pin, Timer
from time import sleep
from neopixel import Neopixel

led = Pin(10, Pin.OUT)
timer = Timer()

## num_leds, state_machine, pin, mode
pixels = Neopixel(1, 0, 23, "RGB")

def blink(timer):
    led.toggle()

def wheel(pos):
    ## Input a value 0 to 255 to get a color value.
    ## The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
 
 
def rainbow_cycle(p, wait):
    for j in range(255):
        p.set_pixel(0, wheel(j))
        p.show()
        sleep(wait)
 
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

pixels.clear()
pixels.brightness(1)
pixels.set_pixel(0, (255, 0, 255))
pixels.show()

while True:
    rainbow_cycle(pixels,0.01)
"""
