import requests
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('text', type=str, location='args')
parser.add_argument('user_id', type=str, location='args')
texts = {}
i = 0

class Post(Resource):
    def post(self):
        args = parser.parse_args()
        global i  # Declare 'i' as a global variable
        comment = args['text']
        user_id = args['user_id']
        print(comment)
        print(user_id)
        ai_url = 'http://127.0.0.1:5000/AI'
        ai_response = requests.post(ai_url, params={'text': comment})
        if ai_response.status_code == 200:
            try:
                return ai_response.json(), 200
            except (ValueError, TypeError):
                return {"error": "AI response is not an integer"}, 400
        else:
            return {"error": "AI service error"}, 500
api.add_resource(Post, '/post_text')

class AI(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        com = args['text']
        print(com)
        return {'type': 3}

api.add_resource(AI, '/AI')


if __name__ == "__main__":
    app.run(debug=True)



