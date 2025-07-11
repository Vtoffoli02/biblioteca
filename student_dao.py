from models.student import Student

class StudentDAO:
    #Cadastra um novo aluno
    def create(self,name,age,email):
        return Student.create(name=name, age=age, email=email)
    
    #busca os registros pelo ID
    def get_by_id(self, student_id):
        try:
            return Student.get(Student.id == student_id)
        except Student.DoesNotExist:
            return None
    
    #deleta o registro
    def delete(self, student_id):
        student = self.get_by_id(student_id)

        if student:
            student.delete_instance()
            return True
        
    #Atualiza o registro

    #busca todos os registros
 