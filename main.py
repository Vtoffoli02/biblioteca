import sys
import os

PROJECT_DIR = "C:\\Projetos\\studentRegistrationSQL\\"

sys.path.append(os.path.abspath(PROJECT_DIR))

from db.connection import create_tables
import services.student_service as service

#Menu principal
def main_menu() -> str:
    print("\n Sistema de Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Aluno")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

    opcao:str = input("Escolha uma opção:")
    return opcao

if __name__ == "__main__":
    create_tables()

    while True:
        opcao = main_menu()

        if opcao == "1":
            name:str = input("Nome:")
            email:str = input("E-mail:")
            age:int = int(input("Idade:"))
            service.create_record(name,email,age)

        elif opcao == "5":
            break
        else:
            print("Opção Invalida")

    