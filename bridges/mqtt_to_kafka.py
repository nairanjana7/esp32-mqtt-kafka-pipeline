import json
import paho.mqtt.client as mqtt
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    producer.send("iot-esp32-work", data)
    print("Forwarded to Kafka:", data)

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("iot/esp32")
client.on_message = on_message

client.loop_forever()
