from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

from svc import message_service

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('from')
parser.add_argument('to')
parser.add_argument('body')
class MsgsHandler(Resource):
    def get(self):
        return message_service.get_all()

    def post(self):
        args = parser.parse_args()
        max_id = message_service.put(args)
        return max_id, 201

class MsgHandler(Resource):
    def get(self, id):
        return message_service.get_by_id(int(id))

    def delete(self, id):
        return message_service.delete(int(id))


api.add_resource(MsgsHandler, '/msg')
api.add_resource(MsgHandler, '/msg/<id>')

if __name__ == "__main__":
    app.run(debug=True)