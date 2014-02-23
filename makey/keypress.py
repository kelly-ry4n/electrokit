import pythoncom, pyHook #pythoncom from pywin32
from pads import pads

def init(out_q):
    ''' Starts up the listening thread and sets the queues'''

    def OnKeyboardEvent(event):
        # This contains the ascii value of a pad event

        a = chr(event.Ascii)

        try:
            pad = pads[a]
        except KeyError:
            return
        
        # This queue is the input for the piezo module
        # This value will eventually be passed back to main, after
        # the note velocity is calculated for the input
        # print pad
        try:
            out_q.put(pad)
        except TypeError:
            pass


    def listen():
        hm = pyHook.HookManager()
        hm.KeyDown = OnKeyboardEvent
        hm.HookKeyboard()
        pythoncom.PumpMessages()

    listen()
