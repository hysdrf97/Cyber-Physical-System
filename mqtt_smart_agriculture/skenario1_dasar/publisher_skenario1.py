# Skenario 1: Komunikasi Dasar Publisher-Subscriber
import paho.mqtt.client as mqtt
import time
import random

BROKER = 'localhost'
PORT   = 1883
TOPIC  = 'farm/kebun_a/soil_moisture'

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='publisher_s1')
client.connect(BROKER, PORT, 60)

print('[Publisher S1] Terhubung ke broker, mulai mengirim data...')

for i in range(5):
    moisture = random.uniform(30.0, 80.0)
    payload  = f'Kelembaban Tanah: {moisture:.2f}%'
    client.publish(TOPIC, payload, qos=0)
    print(f'[Publish] Topik: {TOPIC} | Pesan: {payload}')
    time.sleep(2)

client.disconnect()
print('[Publisher S1] Selesai.')
