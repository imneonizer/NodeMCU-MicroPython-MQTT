# listen to all messages received by mcu
# this script subscribe to special topic where mcu echo all messages

import paho.mqtt.client as mqtt
import argparse
import time

ap = argparse.ArgumentParser()
ap.add_argument("--mqtt", "-m", help="mqtt host", default="192.168.0.90")
ap.add_argument("--port", "-p", help="mqtt port", type=int, default=1883)
ap.add_argument("--topic", "-t", help="subscribe topic", default="/iot/+/mts/logs")
args = ap.parse_args()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    print(f"Subscribed to {args.topic}")
    client.subscribe(args.topic)

def on_message(client, userdata, msg):
    topic = str(msg.topic)
    message = str(msg.payload.decode("utf-8"))
    print(int(time.time()), topic, message)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(args.mqtt, args.port)
client.loop_forever()