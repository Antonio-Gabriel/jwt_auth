from sqlite3 import connect

DATABASE_NAME = "jwt_auth.db"

def get_database_instance():
    connection = connect(DATABASE_NAME)
    connection.execute("PRAGMA foreign_keys = 1")
    return connection