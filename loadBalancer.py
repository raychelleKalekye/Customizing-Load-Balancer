from flask import Flask, jsonify, request
import requests # type: ignore

app = Flask(__name__)

BACKEND_SERVERS = [
    "http://localhost:5003", # Server 1 
    "http://localhost:5001", # Server 2
    "http://localhost:5002"  # Server 3 
]


current_server_index = 0

@app.route('/home', methods=['GET'])
def home():
   
    global current_server_index

    if not BACKEND_SERVERS:
        return jsonify({"error": "No backend servers available"}), 503

   
    server_url = BACKEND_SERVERS[current_server_index]
    current_server_index = (current_server_index + 1) % len(BACKEND_SERVERS)

    try:
        response = requests.get(f"{server_url}/home")
      
        return jsonify(response.json()), response.status_code
    except requests.exceptions.ConnectionError:
        
        return jsonify({"error": f"Server {server_url} is unreachable"}), 500

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return "", 200 

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000)