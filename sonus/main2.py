#  Microphone Module
import machine
import struct
import math

# Constants
REFERENCE_VALUE = 32767  # Maximum value for 16-bit signed integer (for dB calculation)
CALIBRATION_OFFSET = 117  # Offset based on calibration

# Define the pins for the I2S interface
sck_pin = machine.Pin(13)  # Serial clock
ws_pin = machine.Pin(14)   # Word select (LRCLK)
sd_pin = machine.Pin(12)   # Serial data

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

# Function to calculate decibel level from audio samples
def calculate_decibels(samples):
    # Calculate RMS (Root Mean Square)
    rms = math.sqrt(sum(sample ** 2 for sample in samples) / len(samples))
    
    # Ensure RMS is positive to avoid math domain error
    if rms <= 0:
        return float('-inf')  # No signal, return negative infinity (or any other indicator)
    
    # Calculate decibels
    decibels = round(20 * math.log10(rms / REFERENCE_VALUE) + CALIBRATION_OFFSET, 2)
    return decibels

# Buffer to hold microphone data
mic_samples = bytearray(20000)

# Main loop to read data from the microphone
while True:
    num_read = i2s.readinto(mic_samples)
    print("Read {} bytes".format(num_read))
    
    # Convert mic_samples to a list of integers
    samples = struct.unpack('<' + 'h' * (num_read // 2), mic_samples)
    
    # Calculate decibels
    decibels = calculate_decibels(samples)
    
    # Print decibels level
    print("Decibels: {:.2f} dB".format(decibels))
  


#  Clock Module
from machine import I2C, Pin
from urtc import DS1307
from time import sleep

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
rtc = DS1307(i2c)

def show_time(wait):
    (year, month, date, day, hour, minute, second, p1) = rtc.datetime()
    sleep(wait)
    print("""rtc.datetime()""")
    return f"{second:02},{minute:02},{hour:02},{date:02},{month:02},{year}"

def set_time():
    year = int(input("Year: "))
    month = int(input("month (Jan --> 1 , Dec --> 12): "))
    date = int(input("date: "))
    day = int(input("day (1 --> monday , 2 --> Tuesday ... 0 --> Sunday): "))
    hour = int(input("hour (24 Hour format): "))
    minute = int(input("minute: "))
    second = int(input("second: "))
    now = (year, month, date, day, hour, minute, second, 0)
    rtc.datetime(now)

# Mic and RTC
while True:
    num_read = i2s.readinto(mic_samples)
    print("Read {} bytes".format(num_read))
    
    # Convert mic_samples to a list of integers
    samples = struct.unpack('<' + 'h' * (num_read // 2), mic_samples)
    
    # Calculate decibels
    decibels = calculate_decibels(samples)
    
    # Print decibels level
    print("Decibels: {:.2f} dB".format(decibels))
    
    time_string = show_time(1)
    print("Formatted Time:", time_string)

"""
#  MicroSD Module
import machine
import sdcard
import uos

# Assign the chip select (CS) pin (and start it high)
cs_pin = machine.Pin(1, machine.Pin.OUT)

# Initialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=machine.SPI.MSB,
                  sck=machine.Pin(2), mosi=machine.Pin(3), miso=machine.Pin(4))

# Initialize the SD card
sd_card = sdcard.SDCard(spi, cs_pin)

# Mount the filesystem
vfs = uos.VfsFat(sd_card)
uos.mount(vfs, "/sd")

# Create a file and write something to it
with open("/sd/test01.txt", "w") as file:
    file.write("This is a new file on the SD card.\r\n")
    file.write("It's amazing to work with MicroPython and SD cards!\r\n")

# Open the file we just created and read from it
with open("/sd/test01.txt", "r") as file:
    data = file.read()
    print(data)
"""

"""
#  RGB LED
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



