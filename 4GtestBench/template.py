from pylab import *
from rtlsdr import *
import time

while 1:

 sdr = RtlSdr()

 sdr.sample_rate = 240000

 sdr.center_freq = 900e6

 sdr.gain = 'auto'

 samples = sdr.read_samples(128*1024)

 print ('relative power: %0.1f dB' % (10*log10(var(samples))))

 sdr.close()

 time.sleep(0.5)