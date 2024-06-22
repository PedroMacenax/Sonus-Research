#  General
## Gather the noise level and date, put it into a .csv file and save it



#  MicroSD Module



#  Microphone Module
import machine
import struct

# Define the pins for the I2S interface
sck_pin = machine.Pin(14)  # Serial clock
ws_pin = machine.Pin(15)   # Word select (LRCLK)
sd_pin = machine.Pin(13)   # Serial data

# Setup I2S
i2s = machine.I2S(
    0,                      # I2S ID
    sck=sck_pin,            # Serial clock pin
    ws=ws_pin,              # Word select pin
    sd=sd_pin,              # Serial data pin
    mode=machine.I2S.RX,    # Receive mode
    bits=16,                # Sample size in bits
    format=machine.I2S.MONO,# Mono format
    rate=16000,             # Sampling rate
    ibuf=20000              # Internal buffer length
)

# Buffer to hold microphone data
mic_samples = bytearray(20000)

# Main loop to read data from the microphone
while True:
    num_read = i2s.readinto(mic_samples)
    print("Read {} bytes".format(num_read))
    # Process mic_samples here
    # For example, convert to a list of integers:
    samples = struct.unpack('<' + 'h' * (num_read // 2), mic_samples)
    print(samples)


#  Clock Module
from machine import I2C, Pin
from urtc import DS1307
from time import sleep

i2c = I2C(0,scl = Pin(1),sda = Pin(0),freq = 400000)
rtc = DS1307(i2c)

def show_time(wait):
    (year,month,date,day,hour,minute,second,p1)=rtc.datetime()
    utime.sleep(wait)
    print(rtc.datetime())
    

def set_time():
    year = int(input("Year: "))
    month = int(input("month (Jan --> 1 , Dec --> 12): "))
    date = int(input("date: "))
    day = int(input("day (1 --> monday , 2 --> Tuesday ... 0 --> Sunday): "))
    hour = int(input("hour (24 Hour format): "))
    minute = int(input("minute: "))
    second = int(input("second: "))
    now = (year,month,date,day,hour,minute,second,0)
    rtc.datetime(now)

while True:
    show_time(1)
    

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
