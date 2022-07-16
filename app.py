import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
sqlite_default = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(SQLALCHEMY_DATABASE_URI, sqlite_default)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/users", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']
    try:
        new_user = User(username, email)
        db.session.add(new_user)
        db.session.commit()
        result = user_schema.dump(new_user)
    except IntegrityError:
        db.session.rollback()
        result = {"message": "user {} already exists".format(username)}
    return jsonify(result)

@app.route("/users", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@app.route("/users/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@app.route("/users/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']
    user.email = email
    user.username = username
    db.session.commit()
    return user_schema.jsonify(user)

@app.route("/users/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
