import threading
from Queue import Queue
import pyaudio
import numpy as np
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
				output_queue.put(#np.fromstring(old_data,dtype=np.uint32 ##Return Volume
					)
            old_data,curr_data = curr_data, stream.read(chunk)


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

