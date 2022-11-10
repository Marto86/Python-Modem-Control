import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

print([port.description for port in ports])