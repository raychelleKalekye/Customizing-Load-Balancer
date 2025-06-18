from flask import Flask, jsonify, request
import os
import subprocess

app = Flask(__name__)

replicas = []  # this will store the list of running server container names

@app.route("/rep", methods=["GET"])
def get_replicas():
    return jsonify({
        "message": {
            "N": len(replicas),
            "replicas": replicas
        },
        "status": "successful"
      }), 200

@app.route("/add", methods=["POST"])
def add_replicas():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid JSON", "status": "failure"}), 400

    n = data.get("n")
    hostnames = data.get("hostnames")

    if not n or not hostnames or n > len(hostnames):
        return jsonify({
            "message": "<Error> Invalid input or 'n' is greater than hostnames",
            "status": "failure"
        }), 400

    for i in range(n):
        hostname = hostnames[i]
        cmd = f"docker run -d --name {hostname} --network net1 -e SERVER_ID={hostname} flask-server"
        print("Running:", cmd)
        result = os.system(cmd)
        if result == 0:
            replicas.append(hostname)
        else:
            print(f"Failed to spawn {hostname}")

    return jsonify({
        "message": {
            "N": len(replicas),
            "replicas": replicas
        },
        "status": "successful"
    }), 200

@app.route("/rm", methods=["DELETE"])
def remove_replicas():
    data = request.get_json()
    n = data.get("n")
    hostnames = data.get("hostnames")

    if n > len(replicas):
        return jsonify({
            "message": "<Error> Length of hostname list is more than removable instances",
            "status": "failure"
        }), 400

    removed = []

    # Remove requested ones first
    for hostname in hostnames:
        if hostname in replicas:
            cmd = f"docker rm -f {hostname}"
            result = os.system(cmd)
            if result == 0:
                replicas.remove(hostname)
                removed.append(hostname)

    # If more need to be removed, remove from the rest randomly
    while len(removed) < n and len(replicas) > 0:
        to_remove = replicas.pop()
        cmd = f"docker rm -f {to_remove}"
        os.system(cmd)
        removed.append(to_remove)

    return jsonify({
        "message": {
            "N": len(replicas),
            "replicas": replicas
        },
        "status": "successful"
    }), 200
    for i in range(n):
        hostname = hostnames[i]

        # Run the docker container with a unique name and server ID
        cmd = f"docker run -d --name {hostname} --network net1 -e SERVER_ID={hostname} flask-server"
        result = os.system(cmd)

        if result == 0:
            replicas.append(hostname)

    return jsonify({
        "message": {
            "N": len(replicas),
            "replicas": replicas
        },
        "status": "successful"
     }), 200

# Health check endpoint to verify the balancer is running
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Load Balancer is running!"}), 200

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)
