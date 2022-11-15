qrf_band = 'GSM900'
qrf_test_mode_on = 'on'
qrf_chanell = 62
qrf_power = 200

qrf_test_on_command = 'AT+QRFTEST="{}",{},"{}",{}'.format(qrf_band,qrf_chanell,qrf_test_mode_on,qrf_power)  #AT+QRFTEST="GSM900",62,"on",200 
print(qrf_test_on_command)