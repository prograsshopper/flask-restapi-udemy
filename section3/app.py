from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# POST - recieve data
# GET - send data back only

# POST /store data: {name: ..}
@app.route('/store', method=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_store():
    pass

# POST /soitre/<string:name>/ item 
@app.route('/store/<string:name>/item', method=['POST'])
def create_store_in_store(name):
    pass

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass

app.run(port=5000)