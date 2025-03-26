from flask import Blueprint, jsonify, request, send_file
from .report_generator import generate_pdf
import os

report_bp = Blueprint("report", __name__)

@report_bp.route("/api/report", methods=["POST"])
def create_report():
    data = request.json
    pdf_path = generate_pdf(data)
    return jsonify({"message": "PDF generated", "path": pdf_path})

@report_bp.route("/api/report.pdf", methods=["GET"])
def download_report():
    path = "report.pdf"
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return jsonify({"error": "No report found"}), 404
