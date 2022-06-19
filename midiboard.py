
import mido
import requests
from queue import LifoQueue
# WS server example

import asyncio
import websockets

# requests.get("http://192.168.1.126/set/pattern/1")
# inport = mido.open_input("G2V:G2V MIDI 1 14:0")
print(mido.get_output_names())


# inport = mido.open_input("G2V:G2V MIDI 1 20:0")
# 42 is far 41 us bar

def send_get_req(url):
    requests.get(url)


cmdStack = LifoQueue(maxsize=1000)
last_call = 0
cmdStack.put(0)


async def loop():
    uri = "ws://192.168.1.30:81"  # BAR

    # uri2 = "ws://192.168.1.205:81"#192.168.1.205:81 is bar #192.168.1.14:81 is game table light 192.168.1.5

    async with websockets.connect(uri) as websocket:  # , websockets.connect(uri) as websocket:
        with mido.open_input("MPKmini2:MPKmini2 MIDI 1 20:0") as inport:  # 192.168.1.14

            while True:
                for msg in inport:

                    try:

                        if msg.type == "note_on":

                            if msg.note == 44:
                                await websocket.send("ptrn=8")
                                # await websocket2.send("ptrn=8")
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.136/set?ptrn=8",)).start()
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.145/set?ptrn=8",)).start()
                            elif msg.note == 45:
                                await websocket.send("ptrn=1")
                                # await websocket2.send("ptrn=1")
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.126/set?ptrn=1",)).start()
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.145/set?ptrn=1",)).start()
                            elif msg.note == 46:
                                await websocket.send("ptrn=2")
                                # await websocket2.send("ptrn=2")
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.126/set?ptrn=2",)).start()
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.145/set?ptrn=2",)).start()
                            elif msg.note == 47:
                                await websocket.send("ptrn=3")
                                # await websocket2.send("ptrn=3")
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.126/set?ptrn=3",)).start()
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.145/set?ptrn=3",)).start()
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.126/set?ptrn=4",)).start()
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.145/set?ptrn=4",)).start()
                            elif msg.note == 49:
                                await websocket.send("ptrn=5")
                                # await websocket2.send("ptrn=5")
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.126/set?ptrn=5",)).start()
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.145/set?ptrn=5",)).start()
                            elif msg.note == 50:
                                await websocket.send("ptrn=6")
                                # await websocket2.send("ptrn=6")
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.126/set?ptrn=6",)).start()
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.145/set?ptrn=6",)).start()
                            elif msg.note == 51:
                                await websocket.send("ptrn=7")
                                # await websocket2.send("ptrn=7")
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.126/set?ptrn=7",)).start()
                                # threading.Thread(target=send_get_req, args=("http://192.168.1.145/set?ptrn=7",)).start()
                            elif msg.note == 36:
                                await websocket.send("ptrn=9")
                                # await websocket2.send("ptrn=9")
                            elif msg.note == 32:
                                await websocket.send("ptrn=10")
                                # await websocket2.send("ptrn=10")
                                # 123
                            elif msg.note == 37:
                                await websocket.send("ptrn=11")
                                # await websocket2.send("ptrn=11")
                            elif msg.note == 48:
                                await websocket.send("ptrn=13")
                            elif msg.note == 35:
                                await websocket.send("ptrn=14")

                                # await websocket2.send("ptrn=13")

                        if msg.type == "control_change":

                            if msg.control == 1:
                                await websocket.send("brght=" + str(msg.value * 2))
                                # await websocket2.send("brght=" + str(msg.value * 2))
                            if msg.control == 2:
                                await websocket.send("hue=" + str(msg.value * 2))
                                # await websocket2.send("hue=" + str(msg.value * 2))
                            if msg.control == 3:
                                await websocket.send("sat=" + str(msg.value * 2))
                                # await websocket2.send("sat=" + str(msg.value * 2))
                            if msg.control == 4:
                                # await websocket2.send("gen1=" + str(msg.value * 2))
                                await websocket.send("gen1=" + str(msg.value * 2))
                            if msg.control == 5:
                                # await websocket2.send("gen2=" + str(msg.value * 2))
                                await websocket.send("gen2=" + str(msg.value * 2))
                            if msg.control == 6:
                                await websocket.send("gen3=" + str(msg.value * 2))
                                # await websocket2.send("gen3=" + str(msg.value * 2))
                            if msg.control == 7:
                                await websocket.send("gen4=" + str(msg.value * 2))
                                # await websocket2.send("gen4=" + str(msg.value * 2))
                            if msg.control == 8:
                                await websocket.send("sat=" + str(msg.value * 2))
                                # await websocket2.send("sat=" + str(msg.value * 2))

                                # requests.post(("http://192.168.1.126/set?brght=" + str(msg.value * 2)))
                                # if (int(round(time.time() * 1000)) - last_call < 100):
                                #     cmdStack.get()
                                #     cmdStack.put(str(msg.value*2))
                                #     pass
                                # else:
                                #     last_call = (int(round(time.time() * 1000)))
                                #     if(cmdStack.empty()):
                                #         requests.get(("http://192.168.1.126/set?brght=" + str(msg.value*2)))
                                #         # requests.get(("http://192.168.1.145/set?brght=" + str(msg.value * 2)))
                                #     else:
                                #         requests.get(("http://192.168.1.126/set?brght=" + str(cmdStack.get())))
                                # requests.get(("http://192.168.1.145/set?brght=" + str(cmdStack.get())))
                                # threading.Thread(target=send_get_req, args=(("http://192.168.1.126/set?brght=" +   str(msg.value*2)), )).start()





                    except requests.exceptions.ChunkedEncodingError as err:
                        # print(err)
                        print("Oh darn look at that... an error")
                    except requests.exceptions.ConnectionError as err:
                        # print(err)
                        print("Oh darn, the wifi module got upset O:")


asyncio.get_event_loop().run_until_complete(loop())