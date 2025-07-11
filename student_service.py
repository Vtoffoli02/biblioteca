from dao.student_dao import StudentDAO

class StudentService:
    def __init__(self):
        self.dao = StudentDAO()

    #cadastrar um aluno novo
    def register_student(self, name, age, email):
        return self.dao.create(name,age,email)

    #atualizar um aluno ja cadastrado pelo ID
    def update_student(self,student_id,name,age,email):
        print("update aluno")

    #excluir um aluno pelo ID
    def remove_student(self,student_id):
        return self.dao.delete(student_id)

    #buscar todos
    def list_student(self):
        print("lista aluno")