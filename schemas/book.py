from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.book import BookModel
from ma import ma

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True 

