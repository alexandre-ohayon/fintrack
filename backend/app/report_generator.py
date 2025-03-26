from reportlab.pdfgen import canvas
import os

def generate_pdf(data):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{data.get('name', 'client')}_report.pdf")
    c = canvas.Canvas(filename)
    c.drawString(100, 750, f"Financial Report for {data.get('name', 'Client')}")
    c.drawString(100, 730, f"Amount: {data.get('amount', 'N/A')} EUR")
    c.save()
    return filename
