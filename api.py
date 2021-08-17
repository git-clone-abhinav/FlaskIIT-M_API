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

@app.route('/rankers/', methods=['GET'])
def rankers():
    if path.exists("/home/pi/Desktop/FlaskIT-M_API/rankers.csv"):
        data = pd.read_csv('/home/pi/Desktop/FlaskIT-M_API/rankers.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200 #why this one ?
    else:
        return "Resuls yet to be declared", 300

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)