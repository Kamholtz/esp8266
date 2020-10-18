
import network
import time

def connect_wifi(essid :str, password : str) -> bool:
    connected = False
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(essid, password)
        for i in reversed(range(5)):
            if sta_if.isconnected():
                connected = True
                break
            else:
                print("Timing out in... " + str(i) + "s")
                time.sleep(1)
    print('network config:', sta_if.ifconfig())

    return connected

def connect_wifi_ben() -> None:
	return connect_wifi('IPF', 'fuckno1234')

