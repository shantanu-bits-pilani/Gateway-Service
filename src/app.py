import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # This will enable CORS for all routes

AUTH_SERVICE_URL = 'http://auth-service:5000'
CHAT_SERVICE_URL = 'http://chat-service:5001'
USER_SERVICE_URL = 'http://user-service:5002'

client = MongoClient(os.environ.get('MONGO_URI', 'mongodb://mongo:27017/gateway_db'))
db = client.gateway_db

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

def forward_request(url, method='GET', json=None):
    headers = {key: value for key, value in request.headers if key != 'Host'}
    if method == 'GET':
        response = requests.get(url, headers=headers)
    else:
        response = requests.post(url, json=json, headers=headers)
    return response

@app.route('/api/register', methods=['POST'])
def register():
    response = forward_request(f'{AUTH_SERVICE_URL}/register', method='POST', json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/api/login', methods=['POST'])
def login():
    response = forward_request(f'{AUTH_SERVICE_URL}/login', method='POST', json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/api/send', methods=['POST'])
def send_message():
    response = forward_request(f'{CHAT_SERVICE_URL}/send', method='POST', json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/api/messages/<receiver>', methods=['GET'])
def get_messages(receiver):
    response = forward_request(f'{CHAT_SERVICE_URL}/messages/{receiver}')
    return jsonify(response.json()), response.status_code

@app.route('/api/create', methods=['POST'])
def create_user():
    response = forward_request(f'{USER_SERVICE_URL}/create', method='POST', json=request.get_json())
    return jsonify(response.json()), response.status_code

@app.route('/api/profile', methods=['GET'])
def get_profile():
    response = forward_request(f'{USER_SERVICE_URL}/profile')
    return jsonify(response.json()), response.status_code

@app.route('/api/users', methods=['GET'])
def get_users():
    print("in users data", flush=True)
    try:
        response = forward_request(f'{AUTH_SERVICE_URL}/users')
        print(f"hello response => {response}", flush=True)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        print(f"Error fetching users: {e}", flush=True)
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/api/send-request/<r_username>', methods=['POST'])
def send_request(r_username):
    logging.debug(f"Received send request for user ID: {r_username}")
    try:
        response = forward_request(f'{USER_SERVICE_URL}/send-request/{r_username}', method='POST')
        logging.debug(f"Response from user service: {response.json()}")
        return jsonify(response.json()), response.status_code
    except Exception as e:
        logging.error(f"Error sending request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/api/accept-request/<r_username>', methods=['POST'])
def accept_request(r_username):
    response = forward_request(f'{USER_SERVICE_URL}/accept-request/{r_username}', method='POST')
    return jsonify(response.json()), response.status_code

@app.route('/api/withdraw-request/<r_username>', methods=['POST'])
def withdraw_request(r_username):
    response = forward_request(f'{USER_SERVICE_URL}/withdraw-request/{r_username}', method='POST')
    return jsonify(response.json()), response.status_code

@app.route('/api/friends', methods=['GET'])
def get_friends():
    response = forward_request(f'{USER_SERVICE_URL}/friends')
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)