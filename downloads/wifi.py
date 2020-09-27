
import network
def connect_wifi(essid :str, password : str):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(essid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def connect_wifi_ben() -> None:
	connect_wifi('IPF', 'fuckno1234')

