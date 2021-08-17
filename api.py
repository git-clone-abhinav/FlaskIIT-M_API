from flask import Flask
from flask import jsonify
from flask_restful import Api
import os.path
from os import path
import pandas as pd

app = Flask(__name__)
api = Api(app)

@app.route('/hello/', methods=['GET'])
def welcome():
    return "Hello World!"

@app.route('/rankers/')
def rankers():
    if path.exists("ranks.txt"):
        data = pd.read_csv('ranks.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200
    else:
        return "Resuls yet to be declared", 300

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)