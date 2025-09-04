from flask import Flask
app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello from Dockerized CI/CD!"
