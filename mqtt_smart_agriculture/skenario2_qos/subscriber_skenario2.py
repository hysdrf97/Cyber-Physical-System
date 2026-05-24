# Skenario 2: Pengiriman Data dengan QoS Berbeda
import paho.mqtt.client as mqtt

BROKER = 'localhost'
PORT   = 1883
TOPIC  = 'farm/kebun_a/temperature'

def on_connect(client, userdata, flags, rc):
    print(f'[Subscriber S2] Terhubung (rc={rc})')
    client.subscribe(TOPIC, qos=2)
    print(f'[Subscriber S2] Subscribe ke: {TOPIC} dengan QoS 2')

def on_message(client, userdata, msg):
    print(f'[Receive] QoS: {msg.qos} | Topik: {msg.topic} | Pesan: {msg.payload.decode()}')

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='subscriber_s2')
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()
