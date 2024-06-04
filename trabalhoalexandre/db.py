import sqlite3
import matplotlib.pyplot as plt
import pandas as pd


def inicailizarBD():
    conexao = sqlite3.connect('RadCadastro.db')
    cur = conexao.cursor()

    create = ["""
    CREATE TABLE IF NOT EXISTS Aluno 
        ( 
         alunoID INTEGER PRIMARY KEY,  
         nomeAluno VARCHAR(50) NOT NULL,
         nota INTEGER NOT NULL
        );""",
    """CREATE TABLE IF NOT EXISTS  Professores 
        ( 
         professorID INTEGER PRIMARY KEY,  
         nomeProfessor VARCHAR(50)
        );
    """,
    """CREATE TABLE IF NOT EXISTS Curso 
        ( 
         cursoID INTEGER PRIMARY KEY,  
         nomeCurso VARCHAR(50) NOT NULL 
        );""",
    """CREATE TABLE IF NOT EXISTS Disciplina 
        ( 
         disciplinaID INTEGER PRIMARY KEY,  
         nomeDisciplina VARCHAR(50) NOT NULL
        );
    """]

    for i in create:
        cur.execute(i)
        conexao.commit()
    fk_create(cur=cur , conexao=conexao)
    cur.close()
    conexao.close()

def fk_create(cur , conexao):

    try:
        fk_create = ['ALTER TABLE Aluno ADD COLUMN idCurso INTEGER REFERENCES Curso(cursoID);',
            'ALTER TABLE Aluno ADD COLUMN idDisciplina INTEGER REFERENCES Disciplina(disciplinaID);',
            'ALTER TABLE Professores ADD COLUMN idCurso INTEGER REFERENCES Curso(cursoID);',
            'ALTER TABLE Professores ADD COLUMN idDisciplina INTEGER REFERENCES Disciplina(disciplinaID);',
            'ALTER TABLE Disciplina ADD COLUMN idCurso INTEGER REFERENCES Curso(cursoID);']

        for i in fk_create:
            cur.execute(i)
            conexao.commit()
    except sqlite3.OperationalError as e:
        pass

