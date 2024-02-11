import sqlite3
import pandas as pd
from threading import Thread, Lock

class Database:
    cursor = None
    connection = None

    def initialize():
        global conexao
        global cursor

        conexao = sqlite3.connect('pessoa.db')
        cursor = conexao.cursor()

        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS pessoa(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME TEXT NOT NULL,
                IDADE INTEGER,
                DOCUMENTO TEXT NOT NULL,
                TELEFONE TEXT,
                EMAIL TEXT
            )'''
        )

        conexao.commit()

        conexao.close()

    def worker(query, resultado):
        conexao = sqlite3.connect('pessoa.db')
        lock = Lock()
        cursor = conexao.cursor()

        cursor.execute(query)
        if 'SELECT' in query:
            resultado_thread = cursor.fetchall()
            resultado_dict = []
            for i in resultado_thread:
                dicionario = {
                    #'ID': i[0],
                    'NOME': i[1],
                    'IDADE': i[2],
                    'DOCUMENTO': i[3],
                    #'TELEFONE': i[4],
                    #'EMAIL': i[5]
                }
                resultado_dict.append(dicionario)

            with lock:
                resultado.extend(resultado_dict)

        else:
            conexao.commit()
            resultado = []
            
        cursor.close()

    def command(*args):
        resultado = []
        resultado.clear()
        threads = []
        for i in range(1):
            thread = Thread(target=Database.worker, args=(args[0], resultado))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return resultado
