import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks_cwt
from helper import smooth

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 3
#WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in xrange(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(np.fromstring(data,dtype=np.uint16))

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

new_array = np.concatenate(frames)

high_threshold = 32768
low_threshold = 5000
data_max = np.max(new_array)

for i in range(len(new_array)):
	if new_array[i] > high_threshold:
		new_array[i] = 65535 - new_array[i]

#new_array[high] -= 65200
new_array[new_array < low_threshold] = 0
#print find_peaks_cwt(new_array,np.arange(1,10))

from scipy.fftpack import rfft,irfft

almost_derivative = np.diff(smooth(new_array))
plt.plot(smooth(new_array))
plt.show()
plt.plot(almost_derivative)
plt.show()
for i in xrange(len(almost_derivative[:-2])):
	if almost_derivative[i] > 0 and almost_derivative[i+1] < 0:
	    print almost_derivative[i]
plt.subplot(121)
plt.plot(np.concatenate(frames),'o')
plt.subplot(122)
plt.plot(new_array,'o')
plt.show()
plt.plot(rfft(new_array),'o')
plt.show()
#numpy.r_[True, a[1(inlove) < a[:-1]] & numpy.r_[a[:-1] < a[1(inlove), True]