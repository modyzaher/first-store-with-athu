from db import db


class UserModel(db.Model):
    
    __tablename__="users"
     
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(80), unique = True, nullble=False)
    username = db.Column(db.String(80),  nullble=False)
    # password = db.relationship("ItemModel",back_populates ="store",lazy="dynamic")