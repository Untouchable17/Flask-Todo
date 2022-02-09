# start project files setting


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager  # нужен, чтобы создать декоратор, который проверяет авторизован ли пользователь


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(20).hex()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
manager = LoginManager(app)  # тут мы его привязываем к нашему приложению

from sweater import models, routes

db.create_all()

