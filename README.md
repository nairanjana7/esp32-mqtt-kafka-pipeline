# ESP32 → MQTT → Kafka Data Pipeline

This project demonstrates an industry-grade IoT data ingestion pipeline where
edge devices (ESP32) publish sensor data via MQTT, which is then forwarded to
Apache Kafka for scalable event streaming and downstream processing.

## Tech Stack
- ESP32 (simulated)
- MQTT (Mosquitto)
- Apache Kafka (KRaft mode)
- Python (paho-mqtt, kafka-python)

## Use Case
Designed for high-throughput, low-latency IoT systems such as:
- Smart health monitoring
- Edge analytics
- Real-time event streaming
