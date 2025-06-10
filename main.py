
from db.connection import create_table
import services.student_services as service

def main_menu() -> str:
    print("\n Sistema de Cadastro de Alunos")
    print("1, Cadastrar Aluno")
    print("2, Listar Aluno")
    print("3, Atualizar Aluno")
    print("4, Excluir Aluno")
    print("5, Sair")

    opcao:str = input("Escolha uma opção:")
    return opcao

if__name__=="__main__":
    create_table()

    while True:
        opcao == "1":
        name:str = input("Nome:")
        email:str = input("E-mail:")
        age:str = input("Idade:")

        service.create_record(name,email,age)

    elif opcao == "3":
        id = int(input("Informe o ID do aluno que vc quer atualizar"))
        new_name = input("Novo nome")
        new_email = input("Novo e-mail")