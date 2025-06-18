from flask import Flask, jsonify
import os

app = Flask(__name__)

# Read the server ID from an env var (set in the Dockerfile below)
SERVER_ID = os.environ.get("SERVER_ID", "unknown")

@app.route("/home", methods=["GET"])
def home():
    return jsonify({
        "message": f"Hello from Server: {SERVER_ID}",
        "status": "successful"
    }), 200

@app.route("/heartbeat", methods=["GET"])
def heartbeat():
    # empty response is fine
    return "", 200

if __name__ == "__main__":
    # listen on all interfaces inside the container
    app.run(host="0.0.0.0", port=5000)
