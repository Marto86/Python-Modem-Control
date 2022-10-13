import serial
import io
import time
import os
from serial import Serial

signal = serial.Serial(
    port='/dev/ttyUSB2',
    baudrate=115200,
    bytesize=8,
    parity='N',
    timeout=1,
    stopbits=1,
    rtscts=False,
    dsrdtr=False
)
 
signal_text = io.TextIOWrapper(signal, newline='\r\n')
 
signal.write("at+reset\r\n".encode())
 
aaa = "a"      
while not aaa[0]=='+':
    aaa = signal_text.readline().rstrip()
print("ICCID: ", aaa[8:])