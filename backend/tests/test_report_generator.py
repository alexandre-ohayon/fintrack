import os
from app.report_generator import generate_pdf

def test_generate_pdf():
    data = {"name": "TestUser", "amount": 999.99}
    path = generate_pdf(data)
    assert os.path.exists(path)
    os.remove(path)  # clean après test
