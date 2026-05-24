# Skenario 4: Penggunaan Wildcard +
import paho.mqtt.client as mqtt
import time
import random

BROKER  = 'localhost'
PORT    = 1883
sensors = ['soil_moisture', 'temperature', 'light', 'ph']

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='publisher_s4')
client.connect(BROKER, PORT, 60)

print('[Publisher S4] Mengirim semua sensor kebun_a...')
for sensor in sensors:
    topic   = f'farm/kebun_a/{sensor}'
    payload = f'{random.uniform(10, 100):.2f}'
    client.publish(topic, payload, qos=1)
    print(f'  [Publish] {topic} => {payload}')
    time.sleep(1)

print('\n[Publisher S4] Kirim dari kebun_b (tidak ditangkap wildcard kebun_a/+)...')
client.publish('farm/kebun_b/temperature', f'{random.uniform(20,33):.2f}', qos=1)
print('  [Publish] farm/kebun_b/temperature => (dikirim, tidak ditangkap sub)')

client.disconnect()
print('[Publisher S4] Selesai.')
