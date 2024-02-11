from database import Database as db

class PessoaRepositorie():

    def search():
        return db.command("SELECT * FROM pessoa")
    
    def searchById(self, query):
        pass

    def update(self, query, *args):
        return super().update(query)
    
    def insert(*args):
        resultado = []
        db.command("INSERT INTO pessoa (NOME, IDADE, DOCUMENTO) VALUES ('" + args[0] + "', '" + args[1] + "', '" + args[2] + "')", resultado)
        
    
    def delete(self, query):
        return super().delete(query)
    