from peewee import Model, CharField, IntegerField, AutoField
from db.connection import db

#classe é o nosso objeto -->Tipo de Dados definido por nós
#Sempre iniciar com letra maiuscula
class Student(Model):
    name = CharField()
    age = IntegerField()
    email = CharField(unique=True)

    #essa classe tem uma dependencia do arquivo db.connection
    class Meta:
        database = db