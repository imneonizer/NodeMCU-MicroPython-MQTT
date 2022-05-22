import network
import ubinascii

node_id = ubinascii.hexlify(network.WLAN().config('mac'),':').decode().upper()
wifi_ssid = 'imiot'
wifi_pass = 'super_secret'
mqtt_host = '192.168.0.90'
mqtt_port = 1883
sub_topic = b'/iot/stm'
pub_topic = b'/iot/%s/mts' % node_id
log_topic = b'%s/logs' % pub_topic
pin_state_topic = b'%s/pins' % pub_topic
heartbeat_topic = b'%s/heartbeat' % pub_topic 
