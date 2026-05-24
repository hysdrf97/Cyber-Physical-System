# Skenario 4: Subscribe dengan Wildcard +
import paho.mqtt.client as mqtt

BROKER = 'localhost'
PORT   = 1883
TOPIC  = 'farm/kebun_a/+'  # + = tepat SATU level

def on_connect(client, userdata, flags, rc):
    print(f'[Subscriber S4] Terhubung (rc={rc})')
    client.subscribe(TOPIC, qos=1)
    print(f'[Subscriber S4] Subscribe ke: {TOPIC}')
    print('[INFO] Wildcard + hanya menangkap farm/kebun_a/<sensor>')

def on_message(client, userdata, msg):
    sensor = msg.topic.split('/')[-1]
    print(f'[Receive] Sensor: {sensor:15s} | Nilai: {msg.payload.decode()}')

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='subscriber_s4')
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()
