
from flask import Flask, jsonify, request
import pandas as pd
from UserModelDB import UserModelDB

app = Flask(__name__)

models = UserModelDB()
images = pd.read_csv('receipt_images.csv')

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/recomendation')
def recomendation():
    user = request.args.get('user')
    usermodel = models.get_user_model(user)
    
    # ML MAGIC
    result = [
        {'id':'Mushroom-risotto-352492'}
    ] #?
    
    for line in result: 
        line['images'] = images[images['id'] == line['id']]['images'].values[0]
    
    return jsonify(result)