import serial
import time

port = serial.Serial("/dev/ttyAMA0", baudrate=9600)

port.write('\x76') # clear

while True:
  port.write(time.strftime('%H%M'))
  port.write('\x77\x10') # colon on
  time.sleep(1)
  port.write('\x77\x00') # colon off
  time.sleep(1)
