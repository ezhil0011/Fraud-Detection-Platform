from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    transaction = {
        "amount": random.randint(10,5000),
        "transaction_type": random.randint(0,3),
        "account_age_days": random.randint(1,2000),
        "location_risk": random.randint(0,1)
    }

    producer.send("transactions", transaction)
    print("Sent:", transaction)
    time.sleep(2)