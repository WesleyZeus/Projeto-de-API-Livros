from flask import Flask, jsonify, request, render_template
from flask_restx import Api, Resource
from marshmallow import ValidationError


from db import db
from ma import ma

from controllers.book import Book, BookList
from server.instance import server

api = server.api
app = server.app

db.init_app(app)
ma.init_app(app)


def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

api.add_resource(Book,'/books/<int:id>')
api.add_resource(BookList, '/books')


@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':

    server.run()
