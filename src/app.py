import config
import gc
import time
import machine
from common.wifi import connect_wifi
from lib.umqtt import MQTTClient
from probe import probe

client = None

def connect(sleep=0, reset=False):
    if reset:
        machine.reset()
        
    global client
    print('Connecting to MQTT broker.... node_id: %s' % config.node_id)
    time.sleep(sleep)
    try:
        connect_wifi(config.wifi_ssid, config.wifi_pass, check=True)
        client = MQTTClient(config.node_id, server=config.mqtt_host, port=config.mqtt_port)
        client.set_callback(probe)
        client.connect()
        client.subscribe(config.sub_topic)
        print('Connected to %s MQTT broker, subscribed to %s' % (config.mqtt_host, config.sub_topic))
    except OSError:
        pass
    except Exception as e:
        print(e)

connect()
beat_time = time.time()
gc_time = time.time()

while True:
    try:
        client.check_msg()
        
        # publish heart beat signal
        if (time.time() - beat_time) > 1:
            beat_time = time.time()
            client.publish(config.heartbeat_topic, config.node_id.encode())
        
        # call garbage collector
        if (time.time() - gc_time) > 10:
            gc_time = time.time()
            gc.collect()
    except OSError as e:
        connect(1, reset=True)
    except Exception as e:
        print(e)
        time.sleep(5)
        machine.reset()
        