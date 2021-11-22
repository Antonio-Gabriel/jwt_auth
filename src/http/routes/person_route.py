from flask import request, jsonify, Blueprint

from src.repositories import PersonRepository

person_route_bp = Blueprint('api_routes', __name__)

@person_route_bp.route('/', methods=['GET'])
def index():    
    """Preview persons

    Returns:
        [json]: [persons]
    """
    return jsonify({"data": "oi"})
    #return jsonify({"status_code": 200, "data": "response"})

@person_route_bp.route('/person/create', methods=['GET'])
def create_person():    
    
    person_repository = PersonRepository(request_api=request)
    response = person_repository.create_person()
    
    if response == None or response == {}:
        return jsonify({"status_code": 409, "msg": {
            "error": "Error"
        }})    

    return jsonify({"status_code": 200, "data": [response]})