import dao.student_dao as dao 
from models.student import Student

def create_record(name,email,age):
    student = Student(name,email,age)
    dao.insert_student(student)