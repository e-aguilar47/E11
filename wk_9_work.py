import RPi.GPIO as GPIO
import time
import sys
import csv

counts=0
start_time=time.time()
run_time=int(sys.argv[1])

meta_data=['time', 'counts']
filename=sys.argv[2]
file=open(filename,'w',newline='')
writer=csv.writer(file)
writer.writerow(meta_data)

def my_callback(channel):
   global counts
   counts+=1
   print(f"Count detected at {time.time()}")

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.add_event_detect(26, GPIO.FALLING, callback=my_callback)

while (time.time()-start_time)<run_time:
   time.sleep(10)
   counts=0
   print(f"Number of counts measured is {counts}")
 
