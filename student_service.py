import dao.student_dao as dao 
from models.student import Student

def create_record(name:str,email:str,age:int):
    student = Student(name,email,age)

    if age >= 130:
        print("Erro Idade Incorreta")
        return
        
    #chamada para a camada 3 - 
    dao.insert_student(student)

def display_record():
    return dao.get_all_students()
        
def atualizar_alunos():
    dao.update()