from backend.extensions import db
from backend.user.models import User
from flask import jsonify, request

from . import function_base_user


@function_base_user.route("/", methods=["GET"])
def home():
    return "Jay shree ram"


@function_base_user.route("/create", methods=["POST"])
def UserCreate():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    mobile = data.get("mobile")
    password = data.get("password")

    user = User(name=name, email=email, mobile=mobile, password=password)
    db.session.add(user)
    db.session.commit()

    return "User created successfully"


@function_base_user.route("/get", methods=["GET"])
def ListUser():
    user = User.query.all()
    return jsonify(
        [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "mobile": user.mobile,
            }
            for user in user
        ]
    )


@function_base_user.route("/get/<int:id>", methods=["GET"])
def DetailUser(id):
    user = User.query.get(id)
    return jsonify({"name": user.name, "email": user.email, "mobile": user.mobile})


@function_base_user.route("/delete/<int:id>", methods=["DELETE"])
def DeleteUser(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return "User deleted successfully"


@function_base_user.route("/update/<int:id>", methods=["PUT"])
def UpdateUser(id):
    user = User.query.get(id)
    data = request.get_json()
    user.name = data.get("name")
    user.email = data.get("email")
    user.mobile = data.get("mobile")
    db.session.commit()

    return "User updated successfully"


@function_base_user.route("/partial_update/<int:id>", methods=["PATCH"])
def PartialUpdateUser(id):
    user = User.query.get(id)
    data = request.get_json()
    if data.get("name"):
        user.name = data.get("name")
    if data.get("email"):
        user.email = data.get("email")
    if data.get("mobile"):
        user.mobile = data.get("mobile")
    db.session.commit()

    return "User updated successfully"
