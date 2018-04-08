
from flask import Flask, jsonify, request
from Recomender import Recomender
import pandas as pd
from UserModelDB import UserModelDB

app = Flask(__name__)

models = UserModelDB()
images = pd.read_csv('receipt_images.csv')
rec = Recomender('recommandation.csv')

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/recomendation')
def recomendation():
    user = request.args.get('user')
    usermodel = models.get_user_model(user)
    
    results = rec.recommend(usermodel)

    for line in results: 
        line['images'] = images[images['id'] == line['id']]['images'].values[0]
    
    return jsonify(results)