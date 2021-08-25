from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
    
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': f'Item {name} is already in here!'}
        
        data = request.get_json() # error if header is not proper type
        item = {'name': name,   'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'item': items}
    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)