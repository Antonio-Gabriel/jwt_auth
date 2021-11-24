from typing import Type
from datetime import datetime, timedelta
from flask import request, jsonify

import jwt

from src.database import get_database_instance
from src.helpers import SecretPassword, SECRET_KEY


class AuthRepository:

    def __init__(self, request_api: Type[request]):
        self.__request_api = request_api
        self.__connection = get_database_instance()
        self.__cursor = self.__connection.cursor()

    def auth_person(self):
        """Authentication oersin

        Args:
            email (str): email address
            password (str): password
        """

        email, password = self.__request_api.json.values()

        query = """
            select password, name from person p 
            where p.email = ?;
        """

        self.__cursor.execute(query, (email,))
        self.__connection.commit()
        result = self.__cursor.fetchone()

        self.__cursor.close()
        self.__connection.close()

        if result is None:
            return {
                "error": {
                    "msg": "User not found"
                }
            }
        else:
            verify_pass = SecretPassword.password_verify(password, result[0])

            if verify_pass:
                token = jwt.encode({
                    "user": result[1],
                    # Expiration token
                    "expiration": str(datetime.utcnow() + timedelta(seconds=60))
                }, SECRET_KEY)

                # jwt.decode(token, SECRET_KEY, algorithms=["HS256"])                

                return { "token": token }
            else:
                return {
                        "error": {
                        "message": 'Unable to verify',
                        "status_code": 403,
                        "headers": {
                            'WWW-Authenticate': 
                            'Basic realm: "Authentication Failed '
                        }
                    }
                }
