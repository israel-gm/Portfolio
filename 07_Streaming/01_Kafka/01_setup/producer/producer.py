import os
import time
import requests
from confluent_kafka import Producer
from google.transit import gtfs_realtime_pb2

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
TOPIC_NAME = os.getenv("TOPIC_NAME", "mta_gtfs")
MTA_API_URL = os.getenv("MTA_API_URL")

p = Producer({"bootstrap.servers": KAFKA_BROKER})

def delivery_report(err, msg):
    if err is not None:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def fetch_and_publish():
    try:
        print("🔄 Fetching GTFS feed...")
        response = requests.get(MTA_API_URL, timeout=10)
        response.raise_for_status()

        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(response.content)

        for entity in feed.entity:
            # Serialize entity as string (could be trip_update, vehicle, alert, etc.)
            msg_value = str(entity)
            p.produce(TOPIC_NAME, value=msg_value.encode("utf-8"), callback=delivery_report)

        p.flush()
        print(f"📡 Published {len(feed.entity)} messages to Kafka topic '{TOPIC_NAME}'")

    except Exception as e:
        print(f"⚠️ Error fetching/publishing: {e}")

if __name__ == "__main__":
    while True:
        fetch_and_publish()
        time.sleep(30)  # fetch every 30 seconds