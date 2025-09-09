from flask import Flask 
app = Flask(__name__)
@app.route("/")
def home():
    return "hello cloud"
if __name__ == "__main__":
   app.run(host="0.0.0.0")
import socket
from datetime import datetime
@app.route("/status")
def status():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    now = datetime.now().strftime(%Y-%m-%d %H:%M:%S")
    return f"Server: {hostname} | IP: {ip} | Time: {now}"
