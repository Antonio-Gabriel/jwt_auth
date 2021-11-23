from typing import Type
from flask import request
from datetime import datetime

from src.database import get_database_instance
from src.helpers import SecretPassword


class PersonRepository:

    def __init__(self, request_api: Type[request]):
        self.__request_api = request_api
        self.__connection = get_database_instance()
        self.__cursor = self.__connection.cursor()

    def create_person(self):
        """ Create a new person"""

        name, email, password, age = self.__request_api.json.values()

        save_person_query = """
            insert into person (name, email, password, age)
            values (?, ?, ?, ?)
        """

        try:
            self.__cursor.execute(
                save_person_query, (
                    name, email,
                    SecretPassword.password_encrypt(password), 
                    age)
                    )
            self.__connection.commit()
        except:
            return {}
        else:
            self.__cursor.close()
            self.__connection.close()

        return {
            "id": self.__cursor.lastrowid,
            "name": name,
            "email": email,
            "password": SecretPassword.password_encrypt(password),
            "age": age,
            "output": {
                "msg": "person created",
                "created_at": datetime.today()
            }
        }

    def get_person(self):
        """ Get a person from the database """

        storage = []

        query = """
            select *from person p ;
        """

        self.__cursor.execute(query)
        result = self.__cursor.fetchall()

        self.__cursor.close()
        self.__connection.close()

        for person in result:
            storage.append({
                "id": person[0],
                "name": person[1],
                "email": person[2],
                "password": person[3],
                "age": person[4],
            })

        return storage
