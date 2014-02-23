from Queue import Queue
import sys
sys.path += [sys.path[0] + '../../']

from threading import Thread
from Queue import Queue
from piezo.PiezoThreading import VolumeThread
import makey.keypress
import json

def main():

    makey_out_q = Queue()
    piezo_out_q = Queue()

    t = VolumeThread(makey_out_q,piezo_out_q)
    t.start()

    t1 = Thread(target=makey.keypress.init,args=(makey_out_q,))
    t1.start()

    def main_block():
        while True:

            data = piezo_out_q.get(block=True)
            print json.dumps(data)

    t3 = Thread(target=main_block)
    t3.start()

main()