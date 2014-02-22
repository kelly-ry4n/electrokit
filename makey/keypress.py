import pythoncom, pyHook #pythoncom from pywin32
 
def OnKeyboardEvent(event):

    a = chr(event.Ascii)
        
    return True

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
