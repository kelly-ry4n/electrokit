import websocket
import thread
import time
import json

def on_message(ws, message):
    # print message
    json_ar = message.split('\n')

    print json_ar
    for j in json_ar:
        if j:
            print j
        ## do stuff with note here
            print json.loads(j)


def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    print 'connected'


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:8076",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()