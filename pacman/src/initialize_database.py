from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists scores;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table scores (
            id INT primary key,
            player text,
            date text
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)