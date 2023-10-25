import json
import random
from flask import Flask, request, jsonify
from redis import Redis

app = Flask(__name__)

# Connect to Redis
redis = Redis()

# Define a function to generate some random data
def generate_random_data():
    return {
        "id": random.randint(1, 100),
        "name": random.choice(["Hari", "Nandy", "Newton"]),
        "age": random.randint(18, 65)
    }

# Define a route to handle HTTPS requests
@app.route("/", methods=["GET"])
def get_data():
    # Get the data from Redis
    data = redis.get("data")

    # If the data is not in Redis, generate some new data
    if data is None:
        data = generate_random_data()
        redis.set("data", json.dumps(data))

    # Return the data as JSON
    return jsonify(data)

# Start the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
