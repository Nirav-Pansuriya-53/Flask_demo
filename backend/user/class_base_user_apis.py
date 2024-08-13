from backend.extensions import db
from backend.user.models import User
from flask import jsonify, request
from flask.views import MethodView

from . import class_base_user


@class_base_user.route("/", methods=["GET"])
def home():
    return "Jay shree ram"


@class_base_user.route("/user", methods=["POST", "GET"])
@class_base_user.route("/user/<int:id>", methods=["GET", "PUT", "PATCH", "DELETE"])
class BaseUserAPIs(MethodView):

    def post(self, body=None):
        data = request.get_json()
        print(data)
        name = data.get("name")
        email = data.get("email")
        mobile = data.get("mobile")
        password = data.get("password")

        user = User(name=name, email=email, mobile=mobile, password=password)
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Create sucessfully!"}), 201

    def get(self, id=None):
        if id is None:
            users = User.query.all()
            return (
                jsonify(
                    [
                        {
                            "id": user.id,
                            "name": user.name,
                            "email": user.email,
                            "mobile": user.mobile,
                        }
                        for user in users
                    ]
                ),
                200,
            )
        else:
            user = User.query.get(id)
            if user is None:
                return jsonify({"message": "User not found"}), 404
            return (
                jsonify(
                    {
                        "id": user.id,
                        "name": user.name,
                        "email": user.email,
                        "mobile": user.mobile,
                    }
                ),
                200,
            )

    def put(self, id):
        user = User.query.get(id)
        if user is None:
            return jsonify({"message": "User not found"}), 404
        data = request.get_json()
        user.name = data.get("name")
        user.email = data.get("email")
        user.mobile = data.get("mobile")
        db.session.commit()

        return jsonify({"message": "User updated successfully"}), 200

    def patch(self, id):
        user = User.query.get(id)
        if user is None:
            return jsonify({"message": "User not found"}), 404
        data = request.get_json()
        if data.get("name"):
            user.name = data.get("name")
        if data.get("email"):
            user.email = data.get("email")
        if data.get("mobile"):
            user.mobile = data.get("mobile")
        db.session.commit()

        return jsonify({"message": "User updated successfully"}), 200

    def delete(self, id):
        user = User.query.get(id)
        if user is None:
            return jsonify({"message": "User not found"}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
