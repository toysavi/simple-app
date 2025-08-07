from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def index():
    pod_name = os.getenv("HOSTNAME")
    node_name = os.getenv("NODE_NAME", "unknown-node")
    cluster_name = os.getenv("CLUSTER_NAME", "K8s Testing Lab")
    pod_ip = socket.gethostbyname(socket.gethostname())

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{cluster_name}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f0f4f8;
                padding: 50px;
            }}
            .card {{
                background: white;
                padding: 30px;
                margin: auto;
                width: 50%;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #326ce5;
            }}
            .info {{
                margin: 20px 0;
                font-size: 18px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{cluster_name}</h1>
            <div class="info"><strong>Pod Name:</strong> {pod_name}</div>
            <div class="info"><strong>Pod IP:</strong> {pod_ip}</div>
            <div class="info"><strong>Node Name:</strong> {node_name}</div>
        </div>
    </body>
    </html>
    """
