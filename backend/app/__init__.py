from flask import Flask, Response
from flask_cors import CORS
from prometheus_client import Counter, generate_latest

REQUEST_COUNTER = Counter('http_requests_total', 'Total HTTP requests')


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.before_request
    def before_request_func():
        REQUEST_COUNTER.inc()

    @app.route("/metrics")
    def metrics():
        return Response(generate_latest(), mimetype="text/plain")

    from .routes import report_bp
    app.register_blueprint(report_bp)

    return app
