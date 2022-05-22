def get_mac():
    import network
    import ubinascii
    return ubinascii.hexlify(network.WLAN().config('mac'),':').decode()

def get_serial():
    import machine
    import ubinascii
    serial = ''
    for i in machine.unique_id():
        serial += str(i)
    return serial

def get_uuid():
    import machine
    import ubinascii
    return ubinascii.hexlify(machine.unique_id()).decode()

def get_eui():
    import machine
    import ubinascii
    uuid =  ubinascii.hexlify(machine.unique_id()).decode()
    uuid = uuid[0:6] + 'fffe' + uuid[6:]
    return hex(int(uuid[0:2], 16) ^ 2)[2:] + uuid[2:]

def get_ip():
    import network
    return network.WLAN(network.STA_IF).ifconfig()