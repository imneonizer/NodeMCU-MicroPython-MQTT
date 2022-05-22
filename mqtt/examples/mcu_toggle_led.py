import paho.mqtt.client as mqtt
import argparse
import time
import json

ap = argparse.ArgumentParser()
ap.add_argument("--mqtt", "-m", help="mqtt host", default="192.168.0.90")
ap.add_argument("--port", "-p", help="mqtt port", type=int, default=1883)
ap.add_argument("--topic", "-t", help="subscribe topic", default="/iot/stm")
args = ap.parse_args()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect(args.mqtt, args.port)

state = 0
while True:
    state = int((not state))
    msg = json.dumps({"action": "switch", "pins": {'D4': state}})
    client.publish(args.topic, msg)
    time.sleep(0.3)
