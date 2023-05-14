from database_connection import get_database_connection


def drop_tables(connection):
    """Tiputtaa taulut, jos ne ovat jo tietokannassa

    Args:
        connection : Yhteys tietokantaan
    """
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS scores;")

    connection.commit()


def create_tables(connection):
    """Luo tarvittavat taulut tietokantaan

    Args:
        connection : Yhteys tietokantaan
    """
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE scores (id INT PRIMARY KEY, player TEXT, score INT, date TEXT);")

    connection.commit()


def initialize_database():
    """Valmistelee tietokannan käytettäväksi
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
