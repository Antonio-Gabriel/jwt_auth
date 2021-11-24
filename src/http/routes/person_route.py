from flask import request, jsonify, Blueprint

from src.repositories import PersonRepository
from src.repositories import AuthRepository

from src.decorators import is_required_token

person_route_bp = Blueprint('api_routes', __name__)


@person_route_bp.route('/', methods=['GET'])
@is_required_token
def index():
    """Preview persons

    Returns:
        [json]: [persons]
    """

    person_repository = PersonRepository(request_api=request)
    response = person_repository.get_person()

    return jsonify({"status_code": 200, "data": response})


@person_route_bp.route('/person/create', methods=['POST'])
def create_person():
    """Create person route

    Returns:
        [json]: [persons]
    """

    person_repository = PersonRepository(request_api=request)
    response = person_repository.create_person()

    if response == None or response == {}:
        return jsonify({"status_code": 409, "msg": {
            "error": "Error"
        }})

    return jsonify({"status_code": 200, "data": [response]})


@person_route_bp.route('/auth/person', methods=['POST'])
def auth():
    """Authenticate person

    Returns:
        [type]: [token]
    """

    auth_repository = AuthRepository(request_api=request)
    response = auth_repository.auth_person()

    return jsonify(response)


@person_route_bp.route('/persons', methods=['GET'])
@is_required_token
def persons():
    """ Show persons """

    return jsonify({"data": "Show Persons"})
