import os
import psycopg2
import requests
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Configurações via variáveis de ambiente
PORT = int(os.environ.get("PORT", 8002))
DATABASE_URL = os.environ.get("DATABASE_URL")
AUTH_SERVICE_URL = os.environ.get("AUTH_SERVICE_URL")

def get_db_connection():
    if not DATABASE_URL:
        return None
    return psycopg2.connect(DATABASE_URL)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "flag-service"})

@app.route('/flags', methods=['GET'])
def get_flags():
    # Placeholder para demo
    return jsonify([
        {"id": 1, "name": "new-feature", "enabled": True},
        {"id": 2, "name": "dark-mode", "enabled": False}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
