from flask import Blueprint, request, jsonify

from backend import db
from backend.user.model import User

users_bp = Blueprint("users", __name__)


@users_bp.route("/", methods=["POST"])
def register():
    get_json = request.get_json()
    user = User(
        username=get_json.get("username"),
        userpassword=get_json.get("password"),
        mobile=get_json.get("mobile")
    )
    db.session.add(user)
    db.session.commit()

    date = {
        "code": 200,
        "msg": "success",
        "data": {
            "token": "xxx",
            "username": get_json.get("username"),
            "id": user.id
            }
    }

    return jsonify(date)


@users_bp.route("usernames/<string:usernames>/count/", methods=["GET"])
def count(username):
    query_count = User.query.filter_by(username=username).count()
    data = {
        "code": 200,
        "msg": "success",
        "data": {
            "count": query_count
        }
    }
    return jsonify(data)


@users_bp.route("/auths/", methods=["POST"])
def auths():
    request_json = request.json_get()
    user_obj = User.query.filter_by(username=request_json.get("username")).first()

    if user_obj:
        if request_json.password == user_obj.password:
            date = {
                "token": "xxx",
                "id": user_obj.id,
                "username": user_obj.username
            }
        else:
            date = {
                "err_msg": "password error"
            }
    else:
        user_obj = User.query.filter_by(mobile=request_json.get("mobile")).first()
        if user_obj:
            if request_json.password == user_obj.password:
                date = {
                    "token": "xxx",
                    "id": user_obj.id,
                    "username": user_obj.username
                }
            else:
                date = {
                    "err_msg": "password error"
                }
        else:
            date = {
                "err_msg": "mobile error"

            }

    return jsonify(date)







