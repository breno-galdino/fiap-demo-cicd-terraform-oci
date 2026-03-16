import os
import psycopg2
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configurações via variáveis de ambiente
PORT = int(os.environ.get("PORT", 8003))
DATABASE_URL = os.environ.get("DATABASE_URL")
AUTH_SERVICE_URL = os.environ.get("AUTH_SERVICE_URL")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "targeting-service"})

@app.route('/target', methods=['POST'])
def check_targeting():
    data = request.json
    user_id = data.get("user_id")
    # Placeholder para demo: target users with ID ending in even numbers
    is_targeted = int(user_id) % 2 == 0 if user_id and user_id.isdigit() else False
    return jsonify({"targeted": is_targeted})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
