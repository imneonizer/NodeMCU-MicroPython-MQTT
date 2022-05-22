from .blink import blink, led

def start_hotspot(ssid, password, check=False):
    import network
    ap = network.WLAN(network.AP_IF)
    if check and ap.active():
        blink(2, 0.03)    
        return True
    
    ap.active(True)
    led.off()
    try:
        ap.config(essid=ssid, password=password)
    except OSError: pass
    blink(2)
    print("Hostspot Started:", {"ssid": ssid, "password": password})
    return ap.active()

def stop_hotspot():
    import network
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    blink(1)
    print("Hostspot Stopped")
    return True