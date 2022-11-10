import serial
import io
import time
import os
from serial import Serial
import serial.tools.list_ports

curr_at_port = ''
at_cmd = 'AT'
at_rssi = 'AT+CSQ'
response_rssi = "+CSQ:"
sim_error = '+CME ERROR: 10'
sim_mounted = '+CPIN: READY'
at_enable_sim_status = 'AT+QSIMSTAT=1'
at_request_sim_status = 'AT+QSIMSTAT?'
quectel_available = False
com_port = '/dev/ttyUSB1'
at_port = 'Android - Mobile AT Interface'


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
    signal_text = io.TextIOWrapper(signal, newline='\r\n')
    signal.write("AT+CPIN?\r\n".encode())
    time.sleep(1)
    sim_result = signal.read(signal.inWaiting()).decode()
    
    if sim_error in sim_result:
          print("SIM CARD FAIL !!!! \nCheck SIM card please !")
    if sim_mounted in sim_result:            
         print("SIM CARD PASS !!!!!!")
    
    signal.write("AT+CSQ\r\n".encode())#+CSQ: 10,99
    time.sleep(1)
    csq_result = signal.read(signal.inWaiting()).decode()
    if response_rssi in csq_result:
     res = csq_result.split(" ")
     value = res[1].split(",")
     rssi_signal = int(value[0])
     if rssi_signal > 10:
       print("Rssi signal PASS ",rssi_signal)
    
      # signal.write("AT+CPIN\r\n".encode()) #+QSIMSTAT: 1,1 // at+cpin?
    
      # if result == '+CPIN: READY':
      #   print("SIM CARD IS SUCCESSFULLY INSERTED")
    time.sleep(0.5)
    signal.close() 

while 1:
  myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
  time.sleep(5)
  for port in myports:
   print(port)
   if at_port in port[1] and com_port in port[0]:
     quectel_available = True 
     curr_at_port = port[0]
     while quectel_available:
       print("4G Device detected at port",curr_at_port)
       time.sleep(4)
       device_test()
       time.sleep(15)
       break 
   if at_port not in port[1]:
       print("Device Search........ \nPlease Connect 4G USB \n")

   
  

# ('/dev/ttyUSB2', 'Android - Mobile AT Interface', 'USB VID:PID=2C7C:6002 SER=0000 LOCATION=1-2:1.4')
# ('/dev/ttyUSB1', 'Android - Mobile AT Interface', 'USB VID:PID=2C7C:6002 SER=0000 LOCATION=1-2:1.3')
# ('/dev/ttyUSB0', 'Android - Mobile Diag Interface', 'USB VID:PID=2C7C:6002 SER=0000 LOCATION=1-2:1.2')

    






