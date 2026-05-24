# Skenario 1: Komunikasi Dasar Publisher-Subscriber
import paho.mqtt.client as mqtt

BROKER = 'localhost'
PORT   = 1883
TOPIC  = 'farm/kebun_a/soil_moisture'

def on_connect(client, userdata, flags, rc):
    print(f'[Subscriber S1] Terhubung ke broker (rc={rc})')
    client.subscribe(TOPIC, qos=0)
    print(f'[Subscriber S1] Subscribe ke topik: {TOPIC}')

def on_message(client, userdata, msg):
    print(f'[Receive] Topik: {msg.topic} | Pesan: {msg.payload.decode()}')

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='subscriber_s1')
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()
