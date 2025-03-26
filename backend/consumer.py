from kafka import KafkaConsumer
import json
from app.report_generator import generate_pdf

consumer = KafkaConsumer(
    'pdf_generation',
    bootstrap_servers='kafka:9092',
    group_id='pdf-consumers',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest'
)

print("👂 Listening for PDF generation requests...")

for message in consumer:
    data = message.value
    print(f"📥 Received message: {data}")
    generate_pdf(data)
    print("✅ PDF generated")