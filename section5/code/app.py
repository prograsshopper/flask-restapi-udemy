from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'alltherglittersarenotgold'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth



if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True