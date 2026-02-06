# ESP32 → MQTT → Kafka Data Pipeline

This project demonstrates an industry-grade IoT data ingestion pipeline where
edge devices (ESP32) publish sensor data via MQTT, which is then forwarded to
Apache Kafka for scalable event streaming and downstream processing.

## Problem Statement

Modern enterprises ingest real-time data from thousands of distributed edge devices.
Direct ingestion into backend systems creates tight coupling, scalability bottlenecks,
and poor failure isolation.

This project simulates an enterprise-grade solution where edge devices communicate
via MQTT, while Apache Kafka acts as a durable, scalable event backbone that decouples
ingestion from downstream processing.

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

## Architecture Overview

The system follows an edge-to-core event-driven architecture:

ESP32 Devices
     ↓
MQTT Broker(s)
     ↓
MQTT → Kafka Bridge
     ↓
Kafka Topic (Partitions)
     ↓
Multiple Consumer Groups
 
- Edge devices (ESP32 – simulated) publish sensor data via MQTT
- MQTT brokers handle lightweight device communication
- A bridge service forwards MQTT messages into Kafka
- Kafka distributes events to multiple consumer groups independently

