# database class db.Model

from flask_login import UserMixin

from sweater import db, manager


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)

    def __init__(self, text, tags):
        self.text = text.strip()
        self.tags = [
            Tag(text=tag.strip()) for tag in tags.split(',')
        ]


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)         # связь на колонку message.id
    message = db.relationship('Message', backref=db.backref('tags', lazy=True))             # теперь описываем поле message

    # relationship - указываем объект, на который мы будем меппиться
    # backref - обратная ссылка. SQLAlchemy создаст виртуальное поле Post в Tag, в котором будут храниться все посты относящиеся к этой категории
    # lazy - объекты в этой коллекции будут подгружаться по мере необходимости


class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)