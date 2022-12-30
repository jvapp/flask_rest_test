from db import db


# mapping between row in a table to python class and therefore python object
class ItemModel(db.Model):
    # table name
    __tablename__ = "items"

    # columns
    # prepoulated as PK by postgres
    id = db.Column(db.Integer, primary_key=True)
    # cannot create item without a name
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Float(2), unique=False, nullable=False)
    # link between item table and store table, foreign key
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
    # define relationship with StoreModel class and it will auto populate store variable with StoreModel object whos id
    # matches that of the foreign key.
    store = db.relationship("StoreModel", back_populates="items")
    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")
