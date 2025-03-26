import os
from reportlab.pdfgen import canvas


def generate_pdf(data):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, "report.pdf")
    c = canvas.Canvas(filename)
    c.drawString(
        100, 750, f"Financial Report for {data.get('name', 'Client')}"
    )
    c.drawString(
        100, 730, f"Amount: {data.get('amount', 'N/A')} EUR"
    )
    c.save()
    return filename
