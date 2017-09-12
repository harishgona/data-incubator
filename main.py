from flask import Flask, jsonify, request, abort, send_file
from flask_restful import Api, Resource
from itertools import *

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
    def get(self, N, M):
        videos = [i+1 for i in range(N)]
        fellows = [i+1 for i in range(M)]
        if (M<N):
            print(fellows)
            print(videos)
            map1 = [(x,y) for x in fellows for y in videos if x!=y]
            print(map1)
            print("true")
        else:
            print("not valid")
        return jsonify(map1)
    


api.add_resource(videosAPI, '/dataincubator/<int:M>/<int:N>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)