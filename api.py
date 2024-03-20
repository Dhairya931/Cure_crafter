from chat import *
from flask import Flask, request,jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/ask',methods=['GET'])
def respond():
    if request.method == 'GET':
        query=request.args['query']
        m=reply(query)
        print(m) 
    
    return jsonify(m)

app.run(port =3000)