import os
from flask import Flask, jsonify

app = Flask(__name__)
SERVER_ID = os.getenv("SERVER_ID", "UnknownServer")

@app.route('/home', methods=['GET'])
def home():
    return jsonify({
        "message": f"Hello from Server: {SERVER_ID}",
        "status": "successful"
    }), 200

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return "", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
