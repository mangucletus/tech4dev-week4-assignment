from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    # Increment a counter in Redis
    visits = redis_client.incr('visits')
    return f"Hello, Docker! You've visited this page {visits} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
