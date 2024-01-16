from db import db

class ItemModel(db.Model):
    __tablename__="items"
    
    
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(80), unique = True, nullble=False)
    price = db.Column(db.Float(precision=2),unique=False, nullble=False)
    store_id= db.Column( db.models.IntegerField , db.Foregin_key("stores.id") ,unique= False,nullble=False)
    store= db.relationship("StoreModel", back_populates = "items")
    