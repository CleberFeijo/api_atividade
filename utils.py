from models import Pessoas, db_session

#Insere Dados na Tabela Pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Renato', idade=25)
    print(pessoa)
    pessoa.save()

#Realiza consulta na Tabela Pessoa
def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoas = Pessoas.query.filter_by(nome='Cleber').first()
    print(pessoas.idade)

#Altera dados na Tabela Pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Cleber').first()
    pessoa.idade = 29
    pessoa.save()

#Exclui dados na Tabela Pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Cleber').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta()