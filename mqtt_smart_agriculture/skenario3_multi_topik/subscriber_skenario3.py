# Skenario 3: Subscribe ke Beberapa Topik
import paho.mqtt.client as mqtt

BROKER = 'localhost'
PORT   = 1883

TOPICS = [
    ('farm/kebun_a/soil_moisture', 1),
    ('farm/kebun_a/temperature',   1),
    ('farm/kebun_a/light',         1),
    ('farm/kebun_b/soil_moisture', 1),
    ('farm/kebun_b/temperature',   1),
]

def on_connect(client, userdata, flags, rc):
    print(f'[Subscriber S3] Terhubung (rc={rc})')
    client.subscribe(TOPICS)
    for t, q in TOPICS:
        print(f'  -> Subscribe: {t} (QoS {q})')

def on_message(client, userdata, msg):
    print(f'[Receive] {msg.topic:40s} => {msg.payload.decode()}')

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='subscriber_s3')
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()
