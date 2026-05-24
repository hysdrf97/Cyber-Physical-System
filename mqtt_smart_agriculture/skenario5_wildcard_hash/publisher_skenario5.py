# Skenario 5: Penggunaan Wildcard #
import paho.mqtt.client as mqtt
import time
import random

BROKER = 'localhost'
PORT   = 1883

all_topics = [
    'farm/kebun_a/soil_moisture',
    'farm/kebun_a/temperature',
    'farm/kebun_a/light',
    'farm/kebun_b/soil_moisture',
    'farm/kebun_b/temperature',
    'farm/kebun_b/ph',
    'farm/kebun_c/humidity',
]

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='publisher_s5')
client.connect(BROKER, PORT, 60)

print('[Publisher S5] Mengirim data dari semua kebun dan sensor...')
for topic in all_topics:
    payload = f'{random.uniform(10, 100):.2f}'
    client.publish(topic, payload, qos=0)
    print(f'  [Publish] {topic} => {payload}')
    time.sleep(0.8)

client.disconnect()
print('[Publisher S5] Selesai.')
