# model is our internal representation of an entity, some helper, whereas a resource external representaion of an entity
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'  # here we are telling sqlalchemy the name of table where we will store our objects

    id = db.Column(db.Integer, primary_key=True)  # and the columns of table
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    # Here we are realise that this class is API itself. So as long as the methods of API return the same data, changing work of API doesn't 
    # affect the way it can be used. For example, security.py uses this API to interact with database. After refactoring of this API we don't need
    # to change anything in security.py. That is a power of API as interface. 

