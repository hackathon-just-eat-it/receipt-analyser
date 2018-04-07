
from flask import Flask, jsonify, request
from UserModelDB import UserModelDB

app = Flask(__name__)

models = UserModelDB()

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/recomendation')
def recomendation():
    user = request.args.get('user')
    usermodel = models.get_user_model(user)
    
    # ML MAGIC
    result = [] #?
    
    return jsonify(result)