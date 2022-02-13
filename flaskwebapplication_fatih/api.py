# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 21:50:38 2021

@author: fatih
"""

from flask import Flask







    

from flask_restful import Resource, Api
import twitter_tools as tt
import requests



app = Flask(__name__)
api = Api(app)

@app.route('/hello/')
def hello(name):
   info = requests.get('http://localhost:5000/hello/'+name)
   return info.text







class Hello(Resource):
    def get(self, name):
        return {"Hello":name}

class Search(Resource):
    def get(self, name):
        name = "fatihbugra5461"
        person = tt.twitter(name)
        return person

api.add_resource(Search, '/search/<name>')
#api.add_resource(Hello, '/hello/<name>')

if __name__ == '__main__':
    app.run(debug=True)