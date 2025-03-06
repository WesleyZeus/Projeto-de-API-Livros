from flask import Flask, Blueprint
from flask_restx import Api
from marshmallow import ValidationError
from flask_sqlalchemy import SQLAlchemy


class Server():
    def __init__(self, ):

        self.app = Flask(__name__, 
                 template_folder='C:/Users/wesley silva/Desktop/Projeto de API Livros/templates', 
                 static_folder='C:/Users/wesley silva/Desktop/Projeto de API Livros/static')    



        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc', title='Sample flask-SQLAlchemy')
        self.app.register_blueprint(self.blueprint)

        #Parte dos banco de dados!
    

        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        

        self.book_ns = self.api.namespace(name='Books', description='Books related operations', path='/books')

    


    def run(self, ):
        self.app.run(port=5000, debug=True, host='0.0.0.0')


server = Server()
