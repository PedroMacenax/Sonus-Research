#  Microphone Module
import machine
import struct
import math

REFERENCE_VALUE = 32767
CALIBRATION_OFFSET = 117 

# Define the pins for the I2S interface
sck_pin = machine.Pin(13)
ws_pin = machine.Pin(14)
sd_pin = machine.Pin(12)

# Setup I2S
i2s = machine.I2S(
    0,
    sck=sck_pin,
    ws=ws_pin,
    sd=sd_pin,
    mode=machine.I2S.RX,
    bits=16,
    format=machine.I2S.MONO,
    rate=32000,
    ibuf=20000
)



def calculate_decibels(samples):
    rms = math.sqrt(sum(sample ** 2 for sample in samples) / len(samples))
    if rms <= 0:
        return float('-inf')
    decibels = round(20 * math.log10(rms / REFERENCE_VALUE) + CALIBRATION_OFFSET, 2)
    return decibels

mic_samples = bytearray(20000)



def show_decibels():
    num_read = i2s.readinto(mic_samples)
    samples = struct.unpack('<' + 'h' * (num_read // 2), mic_samples)
    decibels = calculate_decibels(samples)
    return decibels

# Clock Module
from machine import I2C, Pin
from urtc import DS1307
from time import sleep

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
rtc = DS1307(i2c)



def show_time(wait=0):
    (year, month, date, day, hour, minute, second, p1) = rtc.datetime()
    weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    weekday = weekdays[day]
    formatted_time = [year,month,date,hour,minute,second,weekday]
    sleep(wait)
    return formatted_time



def set_time():
    year = int(input("Year: "))
    month = int(input("month (Jan --> 1 , Dec --> 12): "))
    date = int(input("date: "))
    day = int(input("day (1 --> Monday , 2 --> Tuesday ... 0 --> Sunday): "))
    hour = int(input("hour (24 Hour format): "))
    minute = int(input("minute: "))
    second = int(input("second: "))
    now = (year, month, date, day, hour, minute, second, 0)
    rtc.datetime(now)



# MicroSD Module
import uos
import sdcard

cs_pin = machine.Pin(5, machine.Pin.OUT)
spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=machine.SPI.MSB,
                  sck=machine.Pin(2), mosi=machine.Pin(3), miso=machine.Pin(4))
sd_card = sdcard.SDCard(spi, cs_pin)
vfs = uos.VfsFat(sd_card)
uos.mount(vfs, "/sd")

while True:
    time_data = show_time()
    decibels = show_decibels()
    data = f"{time_data[0]}, {time_data[1]}, {time_data[2]}, {time_data[3]}, {time_data[4]}, {time_data[5]}, {time_data[6]}, {decibels}\n"
    with open("/sd/data_log.txt", "a") as file:
        file.write(data)
    print(data)


