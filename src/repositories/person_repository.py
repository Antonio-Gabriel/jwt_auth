from typing import Type
from flask import request
from datetime import datetime

from src.database import get_database_instance


class PersonRepository:

    def __init__(self, request_api: Type[request]):
        self.__request_api = request_api
        self.__connection = get_database_instance()

    def create_person(self):
        name, email, password, age = self.__request_api.json.values()

        save_person_query = """
            insert into person (name, email, password, age)
            values (?, ?, ?, ?)
        """

        cursor = self.__connection.cursor()
        try:
            cursor.execute(save_person_query, (name, email, password, age))
            self.__connection.commit()
        except:
            return {}            
        else:
            cursor.close()
            self.__connection.close()

        return {
            "id": cursor.lastrowid,
            "name": name,
            "email": email,
            "password": password,
            "age": age,
            "output": {
                "msg": "person created",
                "created_at": datetime.today()
            }
        }
