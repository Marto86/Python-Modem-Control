from rtlsdr import *

from pylab import *

sdr = RtlSdr()

sdr.sample_rate = 3.2e6

sdr.center_freq = 900e6

sdr.gain = 5

samples = sdr.read_samples(500e3)

print ('relative power: %0.1f dB' % (10*log10(var(samples))))