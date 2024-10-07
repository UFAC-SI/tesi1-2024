import sqlite3
from sqlite3 import Error
class Conexao:
    def get_conexao(self):
        caminho = ('/home/limeira/Universidade/Disciplinas/TESI-I/2024/banco'
                   '/banco.db')
        conexao = None
        try:
            conexao = sqlite3.connect(caminho)
            #print('Conectou!')
        except Error as er:
            print(er)
        return conexao