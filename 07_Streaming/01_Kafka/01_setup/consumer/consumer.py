import os
import time
import pandas as pd
from confluent_kafka import Consumer, KafkaException

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
TOPIC_NAME = os.getenv("TOPIC_NAME", "mta_gtfs")

conf = {
    "bootstrap.servers": KAFKA_BROKER,
    "group.id": "mta-consumer-group",
    "auto.offset.reset": "earliest"
}

c = Consumer(conf)

def process_message(msg):
    """Basic analytics: collect fields into DataFrame"""
    text = msg.value().decode("utf-8")
    return {"raw_message": text, "length": len(text)}

if __name__ == "__main__":
    c.subscribe([TOPIC_NAME])
    print(f"🟢 Subscribed to topic {TOPIC_NAME}")

    buffer = []

    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            
            data = process_message(msg)
            buffer.append(data)

            # Every 50 messages, print a quick summary
            if len(buffer) >= 50:
                df = pd.DataFrame(buffer)
                print("\n📊 Analytics Snapshot")
                print(df["length"].describe())
                buffer.clear()

    except KeyboardInterrupt:
        pass
    finally:
        c.close()
        print("🛑 Consumer closed")