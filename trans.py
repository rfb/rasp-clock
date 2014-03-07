import serial
import time

port = serial.Serial("/dev/ttyAMA0", baudrate=9600)

port.write('\x76') # clear

time.sleep(1)

sleeptime = 0.3
shortsleep = 0.05

""" multiline

port.write('\x7B') # digit 1
port.write('\x06') # 1
time.sleep(sleeptime)

time.sleep(1)

port.write('\x7B') # digit 1
port.write('\x0c') # digit 1
time.sleep(sleeptime)

port.write('\x7B') # digit 1
port.write('\x18') # digit 1
time.sleep(sleeptime)

port.write('\x7B') # digit 1
port.write('\x58') # digit 1
time.sleep(sleeptime)

port.write('\x7B') # digit 1
port.write('\x5A') # digit 1
time.sleep(sleeptime)

port.write('\x7B') # digit 1
port.write('\x5B') # 2
time.sleep(sleeptime)

time.sleep(1)

port.write('\x7B') # digit 1
port.write('\x58') # digit 1
time.sleep(sleeptime)

port.write('\x7B') # digit 1
port.write('\x09') # digit 1
time.sleep(sleeptime)

port.write('\x7B') # digit 1
port.write('\x43') # digit 1
time.sleep(sleeptime)

port.write('\x7B') # digit 1
port.write('\x4F') # 3
time.sleep(sleeptime)

time.sleep(1)

port.write('\x7B') # digit 1
port.write('\x6e')
time.sleep(sleeptime)

port.write('\x7B') # digit 1
port.write('\x66') # 4
time.sleep(sleeptime)

time.sleep(1)

port.write('\x7B') # digit 1
port.write('\x7E') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6F') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x7E') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6D') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6F') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6D') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6F') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6F') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x7E') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6D') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6F') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6D') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6F') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6D') # 5
time.sleep(shortsleep)

time.sleep(1)
"""

port.write('\x7B') # digit 1
port.write('\x5C') # 5
time.sleep(sleeptime)

port.write('\x7E') # digit 1
port.write('\x01') # 5
time.sleep(sleeptime / 2)

port.write('\x7E') # digit 1
port.write('\x00') # 5
port.write('\x7D') # digit 1
port.write('\x01') # 5
time.sleep(sleeptime / 2)

port.write('\x7D') # digit 1
port.write('\x00') # 5
port.write('\x7C') # digit 1
port.write('\x01') # 5
time.sleep(sleeptime / 2)

port.write('\x7C') # digit 1
port.write('\x00') # 5
port.write('\x7B') # digit 1
port.write('\x5D') # 5
time.sleep(sleeptime)

port.write('\x7B') # digit 1
port.write('\x7D') # 6!
time.sleep(sleeptime)

port.write('\x7B') # digit 1
port.write('\x3D') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6D') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x75') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x79') # 4
time.sleep(shortsleep)

#one rotation

port.write('\x7B') # digit 1
port.write('\x3D') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x6D') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x75') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x79') # 4
time.sleep(shortsleep)

#without 6 this time

port.write('\x7B') # digit 1
port.write('\x1D') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x4D') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x55') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x59') # 4
time.sleep(shortsleep)

# and wrap it up

port.write('\x7B') # digit 1
port.write('\x1D') # 4
time.sleep(shortsleep)

port.write('\x7B') # digit 1
port.write('\x07') # 7
time.sleep(sleeptime)
