from .blink import blink, led

def connect_wifi(ssid, password, check=False, scan=False, timeout=10):
    import network
    import time
    
    st = network.WLAN(network.STA_IF)
    st.active(True)
    
    if check and st.isconnected():
        return True
    
    if scan:
        print("Scanning wifi...")
        networks = st.scan()
        AUTHMODE = {0: "open", 1: "WEP", 2: "WPA-PSK", 3: "WPA2-PSK", 4: "WPA/WPA2-PSK"}
        for i, (found_ssid, bssid, channel, rssi, authmode, hidden) in enumerate(sorted(networks, key=lambda x: x[3], reverse=True)):
            found_ssid = found_ssid.decode('utf-8')
            print("%s. ssid: %s chan: %d rssi: %d authmode: %s" % (i+1, found_ssid, channel, rssi, AUTHMODE.get(authmode, '?')))
            
            if found_ssid.lower().startswith(ssid.lower()):
                # connect to wifi if partial name matches
                print("Connecting to...", found_ssid)
                st.connect(found_ssid, password)
                break
    else:
        print("Connecting to...", ssid)
        st.connect(ssid, password)

    led.off()
    t = time.ticks_ms()
    while not st.isconnected():
        if time.ticks_diff(time.ticks_ms(), t) > (timeout*1000):
            blink(2, s=0.5)
            print("Timeout. Could not connect.")
            st.disconnect()
            return False
    
    blink(2)
    print('network config:', st.ifconfig())
    return st.isconnected()

def disconnect_wifi():
    import network
    st = network.WLAN(network.STA_IF)
    st.disconnect()
    st.active(False)
    blink(1)
    print("Wifi Disconnected")
    return True