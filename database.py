import sqlite3

def initialize():
    connection = sqlite3.connect('pessoa.db')

    cursor = connection.cursor()

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS pessoa(
            ID INTEGER PRIMARY KEY,
            NOME TEXT NOT NULL,
            IDADE INTEGER,
            DOCUMENTO TEXT NOT NULL,
            TELEFONE TEXT,
            EMAIL TEXT
        )'''
    )

    connection.commit()