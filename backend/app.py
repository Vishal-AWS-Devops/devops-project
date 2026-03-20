from flask import Flask
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)

r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def index():
    r.incr('hits')
    return f"Hello from Vishal Devops Server 🚀<br>Visits: {r.get('hits').decode()}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
