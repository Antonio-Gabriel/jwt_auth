from flask import Flask
from flask_cors import CORS

from src.http.routes import person_route_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = "f5225ab1413c41a1a4649c8910e19d01"

CORS(app)

app.register_blueprint(person_route_bp)