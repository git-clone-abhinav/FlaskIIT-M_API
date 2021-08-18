from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_cors import CORS, cross_origin
import os.path
from os import path
import pandas as pd

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#api = Api(app)

@app.route('/hello/', methods=['GET'])
@cross_origin()
def welcome():
    return "Hello World!"

@app.route('/rankers/', methods=['GET'])
@cross_origin()
def rankers():
    if path.exists("/home/pi/Desktop/FlaskIT-M_API/rankers.csv"):
        data = pd.read_csv('/home/pi/Desktop/FlaskIT-M_API/rankers.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200 #why this one ?
    else:
        return "Resuls yet to be declared", 300

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)