import time
from flask import Flask, request
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.formatter import FlaskLogstashFormatter
from logstash import TCPLogstashHandler
import logging

app = Flask(__name__)

def logJsonObject(request):
    
     extra = {
        'request_method': request.method,
        'request_scheme': request.scheme,
        'request_host': request.host,
        'request_path': request.path,
        'request_query_string': request.query_string,
        'request_remote_addr': request.remote_addr,
        'request_user_agent': request.user_agent.string,
        'request_referrer': request.referrer
        }
     return extra



@app.route('/')
def hello_world():
    start_time = time.time()
    meta = logJsonObject(request)
    meta['user_data'] = request.args.to_dict()
    meta['response_time'] = (time.time() - start_time) * 1000
    logger.info("test@gmail.com", extra=meta)

    return 'Hello, World!'


if __name__=="__main__":
    jwttoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAZ21haWwuY29tIn0.mc2uE4aoUm032Dl34rhpNxSosjugcApyq-HSGNMXNgU"
    
    logstash_handler = TCPLogstashHandler('localhost',5044,version=1, extra_headers={"Authorization": f"Bearer {jwttoken}"},)
    logstash_handler.formatter = FlaskLogstashFormatter()

    logger = logging.getLogger('flask_app')
    logger.setLevel(logging.INFO)
    logger.addHandler(logstash_handler)
    app.run()


import jwt

API_KEY = "my-secret-api-key"
JWT_SECRET = "my-jwt-secret-key"

def generate_token():
    payload = {
        'api_key': API_KEY
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
    return token


# LOGSTASH_HOST = "0.0.0.0"
# LOGSTASH_DB_PATH = "/home/rohit/Rohit/FlaskLogger/appdata/flask_logstash.db"
# LOGSTASH_TRANSPORT = "logstash_async.transport.BeatsTransport"
# LOGSTASH_PORT = 5044

# logstash_handler = AsynchronousLogstashHandler(
#     LOGSTASH_HOST,
#     LOGSTASH_PORT,
#     database_path=LOGSTASH_DB_PATH,
#     transport=LOGSTASH_TRANSPORT,
# )

# logstash_handler.setLevel(logging.INFO)

# logstash_handler.formatter = FlaskLogstashFormatter(metadata={"beat": "myapp"})
# app.logger.addHandler(logstash_handler)
# app.logger.setLevel(logging.INFO)