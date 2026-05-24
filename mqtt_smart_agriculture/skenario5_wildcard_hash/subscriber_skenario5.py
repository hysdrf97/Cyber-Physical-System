# Skenario 5: Subscribe dengan Wildcard #
import paho.mqtt.client as mqtt

BROKER = 'localhost'
PORT   = 1883
TOPIC  = 'farm/#'  # # = SEMUA level di bawahnya

def on_connect(client, userdata, flags, rc):
    print(f'[Subscriber S5] Terhubung (rc={rc})')
    client.subscribe(TOPIC, qos=0)
    print(f'[Subscriber S5] Subscribe ke: {TOPIC}')
    print('[INFO] Wildcard # menangkap semua topik di bawah farm/')

def on_message(client, userdata, msg):
    parts  = msg.topic.split('/')
    kebun  = parts[1] if len(parts) > 1 else '-'
    sensor = parts[2] if len(parts) > 2 else '-'
    print(f'[Receive] Kebun: {kebun:10s} | Sensor: {sensor:15s} | Nilai: {msg.payload.decode()}')

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='subscriber_s5')
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()
