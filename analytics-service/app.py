import os
import json
import boto3
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Configurações via variáveis de ambiente
PORT = int(os.environ.get("PORT", 8005))
AWS_SQS_URL = os.environ.get("AWS_SQS_URL")
AWS_DYNAMODB_TABLE = os.environ.get("AWS_DYNAMODB_TABLE", "ToggleMasterAnalytics")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

# Inicializa clientes AWS se as variáveis estiverem presentes
# Nota: No ambiente real OCI, isso pode ser mockado ou usar credenciais específicas
sqs = None
dynamodb = None
if AWS_SQS_URL and AWS_REGION:
    sqs = boto3.client('sqs', region_name=AWS_REGION)
    dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "analytics-service", "timestamp": datetime.now().isoformat()})

@app.route('/events', methods=['POST'])
def record_event():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Adiciona timestamp ao evento
    data['timestamp'] = datetime.now().isoformat()
    
    # Simula envio para SQS/DynamoDB (Placeholder para demo)
    print(f"Recording event: {data}")
    
    # Se configurado, tenta enviar para SQS
    if sqs:
        try:
            sqs.send_message(
                QueueUrl=AWS_SQS_URL,
                MessageBody=json.dumps(data)
            )
        except Exception as e:
            print(f"Error sending to SQS: {e}")

    return jsonify({"message": "Event recorded", "data": data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
