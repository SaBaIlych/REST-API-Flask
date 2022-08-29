from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # we telling sqlalchemy that database will live in the root folder of our project
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # this just turn off flask_sqlalchemy mod tracker, not the sqlalchemy mod tracker itself
app.secret_key = 'savely'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':  # long explanation of it's statement; briefly we just circumvent runnig app when we import app.py from outside
    db.init_app(app)
    app.run(port=5000, debug=True)