#!/usr/bin/env python3

from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

REQUEST_COUNTER = Counter('request_counter', 'Number of requests received')

@app.route('/')
def hello():
    REQUEST_COUNTER.inc()
    return 'Hello World!'

if __name__ == '__main__':
    start_http_server(9090)
    app.run(host='0.0.0.0',port=3001)
