from pylab import *
from rtlsdr import *
from matplotlib import pyplot

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6
sdr.center_freq = 95e6
sdr.gain = 4

samples = sdr.read_samples(256*1024)
print(samples)
sdr.close()

# use matplotlib to estimate and plot the PSD
pyplot.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
# pyplot.xlabel('Frequency (MHz)')
# pyplot.ylabel('Relative power (dB)')

pyplot.show()