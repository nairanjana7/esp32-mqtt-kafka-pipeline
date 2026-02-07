import time
import json
import random
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "esp32/sensor"

DEVICE_ID = f"esp32_sim_{random.randint(1, 1000)}"

client = mqtt.Client()
client.connect(BROKER, PORT)

print(f"ESP32 Simulator started: {DEVICE_ID}")

while True:
    payload = {
        "device_id": DEVICE_ID,
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(30, 80), 2),
        "timestamp": int(time.time())
    }

    client.publish(TOPIC, json.dumps(payload))
    print(f"Published: {payload}")
    time.sleep(1)
