from flask import Flask
import pika
import uuid
import threading

app = Flask(__name__)
queue = {}


@app.route("/")
def calculate():
    return "Hello world"
