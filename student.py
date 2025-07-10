from peewee import Model, CharField, IntegerField, AutoField
from db.connection import db

class Student(Model):
    name = CharField()
    age = IntegerField()
    email = CharField(unique=True)

    class Meta:
        database = db

