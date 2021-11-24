from flask import request, jsonify
import jwt

from functools import wraps
from src.helpers import SECRET_KEY


def is_required_token(func):
    @wraps(func)
    def decorate(*args, **kwargs):
        token = request.args.get("token")
        if not token:
            return jsonify({"alert": "Token is missing!"}), 401

        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({"message": "Invalid Token"}), 403

        return func(*args, **kwargs)
    return decorate
