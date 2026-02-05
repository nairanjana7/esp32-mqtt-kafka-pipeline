## Architecture Overview

ESP32 devices act as data producers and publish sensor readings to an MQTT broker.
A Python-based bridge subscribes to MQTT topics and forwards messages to Apache Kafka.

Kafka acts as the central event streaming backbone, enabling scalability,
fault tolerance, and integration with downstream consumers.
