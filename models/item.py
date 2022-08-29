from db import db

class ItemModel(db.Model):  # this create mapping between the database and these objects (user too)
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)  # add id cause it's very useful to have id of entity
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))  # foreign key give us a control and security, we can't delete store if there items in it
    store = db.relationship('StoreModel')  # property of ItemModel that is the store that matches store_id it it's id

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}
    
    @classmethod
    def find_by_name(cls, name):  # stays class method cause return object of ItemModel class
        return cls.query.filter_by(name=name).first()  # query builder comes from db.Model; query: SELECT * FROM items WHERE name=name LIMIT 1
        #  and it returns ItemModel object

    def save_to_db(self):
        db.session.add(self)  # the session in this instance is a collection of object that we're going to write to the database
        db.session.commit()  # we can add multiple objects to the session and then write them all at one 
        # and then we rename this method from insert to save_to_db or upsert. If we change name or price this method allow us to 
        # update value of object cause ID will remain
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()