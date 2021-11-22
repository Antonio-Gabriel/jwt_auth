from src.database import get_database_instance


def create_tables():
    """
     Creates a table ready to accept our data.
     write code that will execute the given sql statement
     on the database
     """

    connection = get_database_instance()

    query = """        
        CREATE TABLE IF NOT EXISTS person(
            id integer primary key  autoincrement not null,
            name text not null,
            email text not null,
            password text not null,
            age integer not null
        )
    """

    connection.execute(query)
    connection.commit()
    connection.close()
