import config
import network
import time

def enable_ap(enable):
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(enable)
    if enable:
        ap_if.config(**config.AP)

def get_ssid(wlan):
    best = None, None
    for (ssid, _, _, rssi, _, _) in wlan.scan():
        if ssid in config.WIFIS:
            if not best[0] or rssi > best[1]:
                best = ssid, rssi
    return best[0]

def connect(timeout=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # try to find a matching wifi for 3 seconds
    for i in range(3):
        ssid = get_ssid(wlan)
        if ssid is not None:
            break
        time.sleep(1)
    if ssid is None:
        wlan.active(False)
        return False
    wlan.connect(ssid, config.WIFIS[ssid])
    start = time.time()
    while not wlan.isconnected():
        if time.time() - start > timeout:
            wlan.active(False)
            return False
    print('network config:', wlan.ifconfig())
    return True
