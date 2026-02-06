import json
from kafka import KafkaConsumer

KAFKA_TOPIC = "iot-esp32-work"   # change if your topic name is different
BOOTSTRAP_SERVERS = "localhost:9092"

TEMP_THRESHOLD = 25.0  # anomaly rule

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    group_id="anomaly-detector-group",
    auto_offset_reset="latest",
    enable_auto_commit=True
)

print("Anomaly Detector started...")

for message in consumer:
    data = message.value
    temperature = data.get("temperature")
    device_id = data.get("device_id")

    if temperature is not None and temperature > TEMP_THRESHOLD:
        print(
            f"[ALERT] High temperature detected | "
            f"Device: {device_id} | Temp: {temperature}"
        )
