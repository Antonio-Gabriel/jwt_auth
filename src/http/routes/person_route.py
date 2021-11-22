from flask import request, jsonify, Blueprint

person_route_bp = Blueprint('api_routes', __name__)

@person_route_bp.route('/', methods=['GET'])
def index():
    return jsonify({"msg": "welcome"})

@person_route_bp.route('/person/create', methods=['GET'])
def create_person():
    return jsonify({"msg": "welcome"})