import sqlite3

###############################################
# Definicao de Variaveis Globais
###############################################

###############################################
## Definicao de funcoes
###############################################

def main_menu():
    print("\n Sistema de Cadastro de Alunos")
    print("1, Cadastrar Aluno")
    print("2, Listar Aluno")
    print("3, Atualizar Aluno")
    print("4, Excluir Aluno")
    print("5, Sair")

    opcao= input("Escolha uma opção:")
    return opcao

def create_table():
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   idade INTEGER
                   )
        """)
    conexao.commit()
    conexao.close()

def register(nome, email,idade):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    try:
        cursor.execute ("INSERT INTO aluno(nome, email, idade) VALUES (?,?,?)",
                        (nome,email,idade))
        conexao.commit()
        print("Aluno cadastrado com sucesso")
    except sqlite3.IntegrityError:
        print("Email ja cadastrado")
    finally:
        conexao.close()

def display():
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    cursor.execute ("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    conexao.close()

    print("Lista de Alunos cadastrados")

    for aluno in alunos: 
        print(aluno)


if __name__== "__main__":
    create_table()

    while True: 
        opcao = main_menu()

        if opcao == "1":
            nome = input ("Nome")
            email = input("E-mail")
            idade = int(input("idade"))
            register(nome,email,idade)
            
        elif opcao == "2":
            display()
        elif opcao == "5":
            break
        else:
            print("Opcao Invalida")

            
