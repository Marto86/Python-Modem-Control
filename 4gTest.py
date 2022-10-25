import serial
import io
import time
import os
from serial import Serial
import serial.tools.list_ports

curr_at_port = ''
at_cmd = 'AT'
at_rssi = 'AT+CSQ'
at_enable_sim_status = 'AT+QSIMSTAT=1'
at_request_sim_status = 'AT+QSIMSTAT?'
quectel_available = False
at_port = "Quectel USB AT Port"
quectel_available = False

def device_test():
    
    signal = serial.Serial(
    port=curr_at_port,
    baudrate=115200,
    bytesize=8,
    parity='N',
    timeout=1,
    stopbits=1,
    rtscts=False,
    dsrdtr=False
)

    signal.write("AT+CPIN?\r\n".encode())
    time.sleep(1)
    pin_result= signal.read(signal.inWaiting()).decode('utf-8')
    print(pin_result)
    if pin_result == '+CME ERROR: 10':
       print("SIM CARD FAIL !!!!!!!!!!!!!!!!!")
      
    if pin_result == '+CPIN: READY':
       print("SIM CARD PASS !!!!!!")
  
  
    signal.write("AT+CSQ\r\n".encode())#+CSQ: 10,99
    time.sleep(1)
    rssi_result= signal.read(signal.inWaiting()).decode('utf-8')
    print(rssi_result)
      # signal.write("AT+CPIN\r\n".encode()) #+QSIMSTAT: 1,1 // at+cpin?
    
      # if result == '+CPIN: READY':
      #   print("SIM CARD IS SUCCESSFULLY INSERTED")
    time.sleep(0.5)
    signal.close() 

while 1:
  myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
  time.sleep(1)
  for port in myports:
   if at_port not in port[1]:
       print("Searching For device.......................")
       
   if at_port in port[1]:
     curr_at_port = port[0]
     print("The current AT commands port is ",curr_at_port)
     device_test()
   
  



    






