from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')  # this is list of item models - many-to-one relationship; many items in one store
    # we set lazy='dynamic' property to avoid long process of creating item objects for each item when we create store model
    # instead we leave this long procedure on json method

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}  # self.items now is query builder 
        # (after we set up lazy property) that have ability to look in items table so now to get list of items we need .all method
    
    @classmethod
    def find_by_name(cls, name): 
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)  
        db.session.commit() 
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()