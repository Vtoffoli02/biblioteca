import sys
from pathlib import Path



#pega o caminho do arquivo atual no caso main.py
current_file = Path(__file__)

#define a raiz do projeto
project_root = Path(__file__).parent.parent

#adiciona a raiz do projeto no path do python
sys.path.append(str(project_root))

from db.connection import connect_db, close_db
from services.student_service import StudentService

def show_menu():
    print("\n===== Sistema de cadastro de Alunos ====")

    print("1. Cadastrar Aluno")
    print("2. Listar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

    print("=========================================")

def main():
    connect_db()

    service = StudentService()

    while True:
        show_menu()

        opcao = input("Escolha a opção:")

        if opcao == "1":
            name = input("Informe o nome:")
            age = int(input("Informe a idade:"))
            email = input("Informe o email:")
            #chama a segunda camada(service) e passa os dados
            service.register_student(name,age,email)

            print("Aluno Cadastrado com sucesso!!")

        elif opcao == "4":
            id = int(input("Informe o id para deletar:"))
            service.remove_student(id)

        elif opcao == "5":
            print("Saindo do sistema")
            break
        else:
            print("opcao invalida")

        close_db() #fecha a conexao com o db

if __name__ == "__main__":
    main()
