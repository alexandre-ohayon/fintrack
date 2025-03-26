from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

data = {
    "name": "Alexandre",
    "amount": 3000
}

producer.send('pdf_generation', value=data)
producer.flush()
print("✅ Message sent")
