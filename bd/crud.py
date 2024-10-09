from conexao import Conexao
from sqlite3 import Error
class Crud:
    def __init__(self):
        self.conexao = Conexao()
    #inserir
    #conectar, usar a conexao e fechar
    def insert(self, sql):
        #sql = """INSERT INTO cliente (nome, cpf, email)
        #         VALUES ('Fulano','123','fulano@ufac.br');
        #      """
        try:
            con = self.conexao.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1:
                con.commit()
                #print('Registro inserido com sucesso!')
            con.close()
            return cursor.rowcount
        except Error as er:
            print(er)

    #listar
    def get(self, sql):
        #sql = """SELECT * FROM cliente;"""
        try:
            con = self.conexao.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall() #Retorna uma lista
            con.close()
            return resultado
        except Error as er:
            print(er)
    #atualizar
    def update(self):
        sql = """UPDATE cliente SET nome='Ciclano', email='ciclano@ufac.br'
                 WHERE id=21;
              """
        try:
            con = self.conexao.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1:
                con.commit()
                print('Registro atualizado com sucesso!')
            con.close()
        except Error as er:
            print(er)
    #excluir
    def delete(self):
        sql = """DELETE FROM cliente WHERE id=22;"""
        try:
            con = self.conexao.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1:
                con.commit()
                print('Registro excluído com sucesso!')
            con.close()
        except Error as er:
            print(er)

#Teste de conexao
#teste = Conexao().get_conexao()
#crud = Crud()
#crud.insert()
#crud.delete()
#crud.update()
#lista = crud.get()
#for item in lista:
#    print(item)