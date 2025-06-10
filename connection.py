import sqlite3
from contextlib import contextmanager

DB_NAME = "C:\Projetos\studentRegistrationSQL\databases\students.db"

@contextmanager
def get_cursor():
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    try:
        yield cursor
        conexao.commit()    
    except sqlite3.ProgrammingError as e:
        conexao.rollback()
        print(f"ocorreu um erro de programação: {e}")
        raise
    except sqlite3.OperationalError as e:
        conexao.rollback()
        print(f"ocorreu um erro do D. operacional{e}")
        raise
    except sqlite3.DatabaseError as e:
        conexao.rollback()
        print(f"ocorreu um erro de banco de dados: {e}")
        raise
    except Exception as e:
        conexao.rollback()
        print(f"erro inesperado: {e}")
        raise
    finally:
        conexao.close()

    def create_table():
        with get_cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS aluno(
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             nome TEXT NOT NULL,
                             email TEXT NOT NULL UNIQUE,
                             idade INTEGER
                        )
                """)
   