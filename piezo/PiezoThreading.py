import threading
from Queue import Queue
import pyaudio
import numpy as np
from helper import smooth, noise_cancel
#from scipy.fftpack import rfft

class PiezoThread(threading.Thread):
	def run(self,input_queue,output_queue,chunk=1024,channels=1,sample_rate=44100):
		controller = pyaudio.PyAudio()
		stream     = controller.open(format = pyaudio.paInt32,
                                   channels = channels,
                                       rate = sample_rate,
                                      input = True,
                          frames_per_buffer = chunk)
		curr_data = None
		while True:
			if not input_queue.empty()
				input_queue.get()

				data = np.fromstring(old_data,dtype=np.uint16)
				data = noise_cancel(data)
				smooth_data = smooth(data)

   				vol = self.volume(smooth_data)
				output_queue.put(vol)

            old_data,curr_data = curr_data, stream.read(chunk)

    def volume(self,data):
    	quasi_derivative = np.diff(data)
    	volumes = []
    	old_i = 0
    	for i in xrange(len(quasi_derivative[0:-2])):
    		if quasi_derivative[i] > 0 and quasi_derivative[i+1] < 0:
    			if old_i < i - 500 and data[old_i] < data[i]:
    				old_i = i
    			else:
    				volumes.append(data[old_i]))
		
		return volumes[-1]


class VolumeThread(threading.Thread):
	def run(self,input_queue,output_queue):
		piezo_out = Queue()
		piezo_in  = Queue()
		piezos    = PiezoThread(piezo_in,piezo_out)

		while True:
			drum_number = input_queue.get(block=True)
			piezo_in.put(None)
			volume = piezo_out.get(block=True)
			output_queue.put((drum_number,volume))

