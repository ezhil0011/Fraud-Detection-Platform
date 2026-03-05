from kafka import KafkaConsumer
import json, requests

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

for msg in consumer:
    transaction = msg.value
    r = requests.post("http://localhost:8000/predict", json=transaction)
    print("Fraud result:", r.json())