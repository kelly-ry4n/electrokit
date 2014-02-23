
import threading
import random

def init(in_q,out_q):

    def calculate_vel():
        while True:
            drum = in_q.get(block=True)
            out_q.put([drum, random.randint(0,255)])
    calculate_vel()

