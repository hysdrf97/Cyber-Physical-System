# Skenario 3: Penggunaan Beberapa Topik
import paho.mqtt.client as mqtt
import time
import random

BROKER = 'localhost'
PORT   = 1883

topics = {
    'farm/kebun_a/soil_moisture': lambda: f'{random.uniform(30, 80):.2f}%',
    'farm/kebun_a/temperature'  : lambda: f'{random.uniform(22, 35):.2f} C',
    'farm/kebun_a/light'        : lambda: f'{random.randint(200, 1000)} lux',
    'farm/kebun_b/soil_moisture': lambda: f'{random.uniform(25, 75):.2f}%',
    'farm/kebun_b/temperature'  : lambda: f'{random.uniform(20, 33):.2f} C',
}

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='publisher_s3')
client.connect(BROKER, PORT, 60)

print('[Publisher S3] Mengirim data ke beberapa topik...')
for i in range(3):
    print(f'\n--- Iterasi ke-{i+1} ---')
    for topic, gen in topics.items():
        payload = gen()
        client.publish(topic, payload, qos=1)
        print(f'[Publish] {topic} => {payload}')
    time.sleep(3)

client.disconnect()
print('[Publisher S3] Selesai.')
