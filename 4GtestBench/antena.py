from pylab import *
from rtlsdr import *
from matplotlib import pyplot
import time

sdr = RtlSdr()

# configure device
sdr.sample_rate = 3.2e6

sdr.center_freq = 902e6

sdr.gain = 'auto'

while 1:
 samples = sdr.read_samples(128*1024)

#  print(samples)
 print ('relative power: %0.1f dB' % (10*log10(var(samples))))
 time.sleep(0.5)
#  sdr = RtlSdr()



sdr.close()

# use matplotlib to estimate and plot the PSD
#  pyplot.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6) 
#  pyplot.xlabel('Frequency (MHz)')
#  pyplot.ylabel('Relative power (dB)')

# pyplot.show()