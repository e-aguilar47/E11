import sys
import adafruit_bme680
import time
import board
import RPi.GPIO as GPIO

i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

#run_time=int(sys.argv[1])

start_time=time.time()
print(start_time)

"""
Example sketch to connect to PM2.5 sensor with either I2C or UART.
"""

import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C


reset_pin = None

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

print("Found PM2.5 sensor, reading data...")

import csv
#meta_data=['time','pm10 standard','pm25 standard','pm100 standard']
#file=open('aq_data.csv',"w",newline='')
#writer=csv.writer(file)
#writer.writerow(meta_data)


#combine
filename=sys.argv[2]
file=open(filename,'w',newline='')
writer=csv.writer(file)
meta_data=['Time','pm10 standard','pm25 standard','pm100 standard','temperature','gas','humidity','pressure','altitude','counts']
writer.writerow(meta_data)
print(meta_data)

#time.sleep(120)

def my_callback(channel):
   global counts
   counts+=1
   print(f"Count detected at {time.time()}")
    
counts=0
start_time=time.time()

run_time=int(sys.argv[1])

now=time.time()
while (now-start_time)<run_time:
    time.sleep(10)
    print(f"Number of counts measured is {counts}")
    now=time.time()
    writer.writerow(data_list)
    time.sleep(1)
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.relative_humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)
    
    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("---------------------------------------")

    now=time.time()
    data_out=[now,aqdata['pm10 standard'],aqdata['pm25 standard'],aqdata['pm100 standard'],bme680.temperature,bme680.gas,bme680.relative_humidity,bme680.pressure,bme680.altitude,counts]
    writer.writerow(data_out)

#counts=0
#start_time=time.time()
#run_time=int(sys.argv[1])

#def my_callback(channel):
   #global counts
   #counts+=1
   #print(f"Count detected at {time.time()}")

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.IN)
#GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback)

#while (time.time()-start_time)<run_time:
   #time.sleep(10)
   #print(f"Number of counts measured is {counts}")
   #now=time.time()
   #data_list=[now,counts]
   #writer.writerow(data_list)

file.close()
 
