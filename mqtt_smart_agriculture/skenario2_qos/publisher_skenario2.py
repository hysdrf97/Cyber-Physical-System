# Skenario 2: Pengiriman Data dengan QoS Berbeda
import paho.mqtt.client as mqtt
import time
import random

BROKER = 'localhost'
PORT   = 1883
TOPIC  = 'farm/kebun_a/temperature'

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='publisher_s2')
client.connect(BROKER, PORT, 60)
client.loop_start()

qos_levels = [0, 1, 2]

print('[Publisher S2] Mengirim data dengan QoS berbeda...')
for qos in qos_levels:
    temp    = random.uniform(22.0, 35.0)
    payload = f'Suhu: {temp:.2f} C (QoS {qos})'
    result  = client.publish(TOPIC, payload, qos=qos)
    print(f'[Publish QoS {qos}] {payload} | Status: {result.rc}')
    time.sleep(2)
import time
time.sleep(2)
client.loop_stop()
client.disconnect()
print('[Publisher S2] Selesai.')
