import config
import ujson
from machine import Pin, PWM
import time

pins = {
    "D0": Pin(16),
    "D1": Pin(5),
    "D2": Pin(4),
    "D3": Pin(0),
    "D4": Pin(2),
    "D5": Pin(14),
    "D6": Pin(12),
    "D7": Pin(13),
    "D8": Pin(15),
}

def update_pin_state(client, topic, msg):
    # switch pins on or off
    recv_pin_state = msg.get('pins', {})
    for (k,v) in recv_pin_state.items():
        try:
            pins[k].value(v)
        except Exception as e:
            print(e)
    
    # publish pins state
    p = {k: v.value() for (k,v) in pins.items()}
    client.publish(config.pin_state_topic, ujson.dumps(p))

def probe(client, topic, msg):
    # decode message and get node_id
    msg = ujson.loads(msg)
    node_id = msg.get('node_id', 'all')
    
    # filter messages based on node_id
    if node_id not in [config.node_id, 'all']:
        return
    
    # log filtered messages
    print(topic, msg)
    client.publish(config.log_topic, ujson.dumps(msg))
    
    # callbacks for actions
    if msg.get('action') == 'switch':
        update_pin_state(client, topic, msg)