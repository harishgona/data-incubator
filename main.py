from flask import Flask, jsonify, request, abort, send_file
from flask_restful import Api, Resource
from itertools import *
import random
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)



@app.route("/")
def forecast():
    return send_file('templates/index.html')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response
def options (self):
    return {'Allow' : 'PUT' }, 200, \
    { 'Access-Control-Allow-Origin': '*', \
      'Access-Control-Allow-Methods' : 'PUT,GET' }

class videosAPI(Resource):
  def get(self, x, y):
    N = int(y)
    people = [i+1 for i in range(N)]
    mapping = []
    popList = {}
    for p in people:
      popList[p] = int(x)

    for p in people:
      M = int(x)
      #peopleList = [i+1 for i in range(N)]
      pushList = []
      while (M>0):
        r = random.randint(1,N)
        #random.seed(r)
        if p!=r and popList[r]>0:
          mapping.append((p,r))
          popList[r] = popList[r]-1
          M = M-1
          print M
        print r
    print(popList)
    print(mapping) 
    return jsonify(mapping)  
        
        
    


api.add_resource(videosAPI, '/<string:x>/<string:y>')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=80)