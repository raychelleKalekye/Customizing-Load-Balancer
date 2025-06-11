import os
from flask import Flask, jsonify, request

app = Flask(__name__)

SERVER_ID = os.getenv("SERVER_ID", "UnknownServer") 

@app.route('/home', methods=['GET'])
def home():
   
    response_data = {
        "message": f"Hello from Server: {SERVER_ID}",
        "status": "successful"
    }
    return jsonify(response_data), 200

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    
    return "", 200 

if __name__ == '__main__':
 
    app.run(host='0.0.0.0', port=5000)