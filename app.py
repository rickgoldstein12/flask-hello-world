#!/usr/bin/env python
# encoding: utf-8

import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def query_records():
    return jsonify({'X': '1'})

@app.route('/')
def hello_world():
    return 'Hello, World!'


# app.run(debug=True)