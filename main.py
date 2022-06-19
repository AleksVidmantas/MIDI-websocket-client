
import mido

import requests
from queue import LifoQueue
# requests.get("http://192.168.1.126/set/pattern/1")
# inport = mido.open_input("G2V:G2V MIDI 1 20:0")
print(mido.get_output_names())
# inport = mido.open_input("G2V:G2V MIDI 1 20:0")

def send_get_req(url):
    requests.get(url)


cmdStack = LifoQueue(maxsize = 500)
last_call = 0
cmdStack.put(0)

with mido.open_input("MPKmini2:MPKmini2 MIDI 1 14:0")as inport:
    while True:
        for msg in inport:
            print(msg)