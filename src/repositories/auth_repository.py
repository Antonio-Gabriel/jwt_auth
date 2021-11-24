from typing import Type
from flask import request

from src.database import get_database_instance
from src.helpers import SecretPassword


class AuthRepository:

    SECRET_KEY = "f5225ab1413c41a1a4649c8910e19d01"

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
            select password from person p 
            where p.email = ?;
        """

        self.__cursor.execute(query, (email,))
        self.__connection.commit()
        result = self.__cursor.fetchone()

        self.__cursor.close()
        self.__connection.close()

        if result is None:
            print("None")
        else:            
            verify_pass = SecretPassword.password_verify(str(result[0]), password)
            print(verify_pass)
