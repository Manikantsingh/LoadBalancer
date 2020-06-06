import platform
import random
import subprocess
import sqlalchemy as db
import pymysql
import math
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from dboperations import savequery

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello_world! This server handles string operations"

@app.route('/reverse')
def reverse():
    try:
        result = ""
        input = str(request.args.get('evalstring'))
        for i in input:
            result = i + result
        savequery(input, result)
    except:
        result = "Error"
    return jsonify(result)


@app.route('/length')
def length():
    try:
        result = ""
        input = str(request.args.get('evalstring'))
        result = len(input)
        savequery(input, result)
    except:
        result = "Error"
    return jsonify(result)

@app.route('/concatenate')
def concatenate():
    try:
        result = ""
        query = str(request.args.get('evalstring'))
        input = str(request.args.get('evalstring'))
        input = input.split("+")
        for x in range(len(input)):
            result += input[x]
        savequery(query, result)
    except:
        result = "Error"
    return jsonify(result)


@app.route('/calculate')
def calculate():
    try:
        input = request.args.get('evalstring')
        print(input)
        result = eval(input)
        print(result)
        savequery(input, result)
        temp = result+1
    except TypeError:
        result = "Error"
    except NameError:
        result = "Error"
    # except :
    #     result = "Error"
    return jsonify(result)


if __name__ == '__main__':
    CORS(app)
    app.run(debug=True, host="0.0.0.0" ,port="5002")
    #app.run(debug=True, host="127.12.1.1", port="8080")

