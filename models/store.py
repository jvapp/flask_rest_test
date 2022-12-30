from db import db


# mapping between row in a table to python class and therefore python object
class StoreModel(db.Model):
    # table name
    __tablename__ = "stores"

    # columns
    # prepoulated as PK by postgres, maps to store_id in items table
    id = db.Column(db.Integer, primary_key=True)
    # cannot create item without a name
    name = db.Column(db.String(80), unique=True, nullable=False)
    # items relationship allows each StoreModel object to see all the items associated with it
    # lazy dynamic does not query items. this prevents 2 queries being executed for each store query
    # Cascade all will delete the children (items) of the store when the store is deleted
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")
