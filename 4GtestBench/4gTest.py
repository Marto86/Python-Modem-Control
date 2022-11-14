import serial
import io
import time
from pylab import *
from rtlsdr import *
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

qrf_band = 'GSM900'
qrf_test_mode_on = 'on'
qrf_test_mode_off = 'off'
qrf_chanell = 62
qrf_power = 200

qrf_test_on_command = 'AT+QRFTEST="{}",{},"{}",{}\r\n'.format(qrf_band,qrf_chanell,qrf_test_mode_on,qrf_power)
qrf_test_off_command = 'AT+QRFTEST="{}",{},"{}",{}'.format(qrf_band,qrf_chanell,qrf_test_mode_off,qrf_power)

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
    # signal_text = io.TextIOWrapper(signal, newline='\r\n')
    sdr = RtlSdr()
    sdr.sample_rate = 3.2e6
    sdr.center_freq = 902e6
    sdr.gain = 'auto'

    signal.write("AT+GSN\r\n".encode())
    time.sleep(1.5)
    imei_result = signal.read(signal.inWaiting()).decode()
    
    signal.write("AT+CSQ\r\n".encode())#+CSQ: 10,99
    time.sleep(1.5)
    csq_result = signal.read(signal.inWaiting()).decode()
    if response_rssi in csq_result:
     res = csq_result.split(" ")
     value = res[1].split(",")
     rssi_signal = int(value[0])
     if rssi_signal > 10:
       print("Rssi signal PASS ",rssi_signal)

    signal.write("AT+CPIN?\r\n".encode())
    time.sleep(1)
    sim_result = signal.read(signal.inWaiting()).decode()
    
    if sim_error in sim_result:
          print("SIM CARD FAIL !!!! \nCheck SIM card please !")
          signal.close()
    if sim_mounted in sim_result:
         print("SIM CARD PASS !!!!!!")
    # signal.write("AT+RESET\r\n".encode())     
    # signal.close()    
    # # configure device
        
         signal.write("AT+QRFTESTMODE=0\r\n".encode())
         time.sleep(0.5)
         signal.write("AT+QRFTESTMODE=1\r\n".encode())
         time.sleep(1)
         signal.write(qrf_test_on_command.encode())
         time.sleep(3)
         samples = sdr.read_samples(128*1024)
         signal_value = (10*log10(var(samples)))
         if signal_value > -26.00 and signal_value < -13.00:
           print('Atena Signal PASSS with %0.2f dB !!!!!!!!' % signal_value)
           time.sleep(1)
           signal.write(qrf_test_off_command.encode())
           time.sleep(0.5)
           signal.write("AT+QRFTESTMODE=0\r\n".encode())
           sdr.close()
           time.sleep(1)            
         
    signal.write("AT+RESET\r\n".encode()) 
    time.sleep(0.5)
    signal.close()

   

while 1:
  myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
  time.sleep(3)
  for port in myports:
  #  print(port)
   if at_port in port[1] and com_port in port[0]:
     quectel_available = True 
     curr_at_port = port[0]
     while quectel_available:
       print("4G Device detected at port",curr_at_port)
       device_test()
       time.sleep(5)
       quectel_available = False 
       break 
   if at_port not in port[1]:
       print("Please Connect 4G USB \n")
   
   
  

# ('/dev/ttyUSB2', 'Android - Mobile AT Interface', 'USB VID:PID=2C7C:6002 SER=0000 LOCATION=1-2:1.4')
# ('/dev/ttyUSB1', 'Android - Mobile AT Interface', 'USB VID:PID=2C7C:6002 SER=0000 LOCATION=1-2:1.3')
# ('/dev/ttyUSB0', 'Android - Mobile Diag Interface', 'USB VID:PID=2C7C:6002 SER=0000 LOCATION=1-2:1.2')

    






