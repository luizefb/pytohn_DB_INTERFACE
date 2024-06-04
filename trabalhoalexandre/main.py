import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import db

db.inicailizarBD()

#Função para deletar ALUNO
def del_aluno(nomeAluno):
    if not nomeAluno:
        messagebox.showwarning("Input Error", "Erro ao inserir")
        return
    con = sqlite3.connect('RadCadastro.db')
    c = con.cursor()
    c.execute("DELETE FROM Aluno WHERE nomeAluno = ?", (nomeAluno,))
    con.commit()
    con.close()
    messagebox.showinfo("Sucesso!", "Aluno deletado!")

def upd_aluno(nomeAluno, nota):
    if not nomeAluno:
        messagebox.showwarning("Input Error", "Erro ao inserir")
        return
    con = sqlite3.connect('RadCadastro.db')
    c = con.cursor()
    c.execute("UPDATE Aluno SET nota = ? WHERE nomeAluno = ?",(int(nota),nomeAluno))
    con.commit()
    con.close()
    messagebox.showinfo("Sucesso!", "Sucesso ao atualizar o Aluno!")

#Função para adicionar o aluno no banco de dados
def adicionar_aluno(nomeAluno, nota, idCurso, idDisciplina):
    if not nomeAluno or not nota:
        messagebox.showwarning("Erro ao adicionar", "Você esqueceu de adicionar os valores")
        return
    con=sqlite3.connect('RadCadastro.db')
    c = con.cursor()
    c.execute("INSERT INTO Aluno (nomeAluno, nota, idCurso, idDisciplina) VALUES (?, ?, ?, ?)", (nomeAluno, int(nota), idCurso, idDisciplina))
    messagebox.showwarning("Atenção", "Aluno cadastrado com sucesso!")
    con.commit()
    con.close()

def del_disciplina(nomeDisciplina):
    if not nomeDisciplina:
        messagebox.showwarning("Input Error", "Erro ao inserir")
        return
    con = sqlite3.connect('RadCadastro.db')
    c = con.cursor()
    c.execute("DELETE FROM Disciplina WHERE nomeDisciplina = ?", (nomeDisciplina,))
    con.commit()
    con.close()
    messagebox.showinfo("Sucesso!", "Disciplina deletada!")

def upd_disciplina(idCurso, nomeDisciplina):
    if not nomeDisciplina:
        messagebox.showwarning("Input Error", "Erro ao inserir")
        return
    con = sqlite3.connect('RadCadastro.db')
    c = con.cursor()
    c.execute("UPDATE Disciplina SET idCurso = ? WHERE nomeDisciplina = ?",((idCurso),nomeDisciplina))
    con.commit()
    con.close()
    messagebox.showinfo("Sucesso!", "Sucesso ao atualizar a disciplina!")

def adicionar_disciplina(nomeDisciplina, idCurso):
    if not nomeDisciplina:
        messagebox.showwarning("Erro ao adicionar", "Você esqueceu de adicionar os valores")
        return
    con=sqlite3.connect('RadCadastro.db')
    c=con.cursor()
    c.execute("INSERT INTO Disciplina (nomeDisciplina, idCurso) VALUES (?, ?)", (nomeDisciplina, idCurso))
    messagebox.showwarning("Atenção", "Disciplina cadastrada com sucesso!")
    con.commit()
    con.close()

def del_curso(nomeCurso):
    if not nomeCurso:
        messagebox.showwarning("Input Error", "Erro ao inserir")
        return
    con = sqlite3.connect('RadCadastro.db')
    c = con.cursor()
    c.execute("DELETE FROM Curso WHERE nomeCurso = ?", (nomeCurso,))
    con.commit()
    con.close()
    messagebox.showinfo("Sucesso!", "Curso deletado!")

def upd_curso(nomeCurso):
    if not nomeCurso:
        messagebox.showwarning("Input Error", "Erro ao inserir")
        return
    con = sqlite3.connect('RadCadastro.db')
    c = con.cursor()
    c.execute("UPDATE Curso SET nomeCurso = ? WHERE nomeCurso = ?",(nomeCurso,nomeCurso))
    con.commit()
    con.close()
    messagebox.showinfo("Sucesso!", "Sucesso ao atualizar o curso!")

def adicionar_curso(nomeCurso):
    if not nomeCurso:
        messagebox.showwarning("Erro ao adicionar", "Você esqueceu de adicionar os valores")
        return
    con=sqlite3.connect('RadCadastro.db')
    c=con.cursor()
    c.execute("INSERT INTO Curso (nomeCurso) VALUES (?)", (nomeCurso,))
    messagebox.showwarning("Atenção", "Curso cadastrado com sucesso!")
    con.commit()
    con.close()

def del_professor(nomeProfessor):
    if not nomeProfessor:
        messagebox.showwarning("Input Error", "Erro ao inserir")
        return
    con = sqlite3.connect('RadCadastro.db')
    c = con.cursor()
    c.execute("DELETE FROM Professores WHERE nomeProfessor = ?", (nomeProfessor,))
    con.commit()
    con.close()
    messagebox.showinfo("Sucesso!", "Professor deletado!")

def upd_professor(idDisciplina, nomeProfessor):
    if not nomeProfessor:
        messagebox.showwarning("Input Error", "Erro ao inserir")
        return
    con = sqlite3.connect('RadCadastro.db')
    c = con.cursor()
    c.execute("UPDATE Professores SET idDisciplina = ? WHERE nomeProfessor = ?",(idDisciplina ,nomeProfessor))
    con.commit()
    con.close()
    messagebox.showinfo("Sucesso!", "Sucesso ao atualizar o professor!")

def adicionar_professor(nomeProfessor, idDisciplina, idCurso):
    if not nomeProfessor:
        messagebox.showwarning("Erro ao adicionar", "Você esqueceu de adicionar os valores")
        return
    con=sqlite3.connect('RadCadastro.db')
    c=con.cursor()
    c.execute("INSERT INTO Professores (nomeProfessor, idDisciplina, idCurso) VALUES (?, ?, ?)", (nomeProfessor, idDisciplina, idCurso))
    messagebox.showwarning("Atenção", "Professor cadastrado com sucesso!")
    con.commit()
    con.close()

def consultar_curso():
    def mostrar_alunos():
        curso_id = combo_cursos.get()
        conexao = sqlite3.connect('RadCadastro.db')
        cur = conexao.cursor()
        cur.execute("SELECT nomeAluno FROM Aluno WHERE idCurso = ?", (curso_id,))
        alunos = cur.fetchall()

        texto_alunos.delete(1.0, tk.END)

        if alunos:
            for aluno in alunos:
                texto_alunos.insert(tk.END, aluno[0] + "\n")
        else:
            texto_alunos.insert(tk.END, "Nenhum aluno matriculado neste curso.")

        cur.close()
        conexao.close()

    def mostrar_disciplinas():
        curso_id = combo_cursos.get()

        conexao = sqlite3.connect('RadCadastro.db')
        cur = conexao.cursor()

        cur.execute("SELECT nomeDisciplina FROM Disciplina WHERE idCurso = ?", (curso_id,))
        disciplinas = cur.fetchall()

        texto_disciplinas.delete(1.0, tk.END)

        if disciplinas:
            for disciplina in disciplinas:
                texto_disciplinas.insert(tk.END, disciplina[0] + "\n")
        else:
            texto_disciplinas.insert(tk.END, "Nenhuma disciplina encontrada para este curso.")

        cur.close()
        conexao.close()

    def mostrar_professores():
        curso_id = combo_cursos.get()

        conexao = sqlite3.connect('RadCadastro.db')
        cur = conexao.cursor()

        cur.execute("SELECT nomeProfessor FROM Professores WHERE idCurso = ?", (curso_id,))
        professores = cur.fetchall()

        texto_professores.delete(1.0, tk.END)

        if professores:
            for professor in professores:
                texto_professores.insert(tk.END, professor[0] + "\n")
        else:
            texto_professores.insert(tk.END, "Nenhum professor encontrado para este curso.")

        cur.close()
        conexao.close()

    window7 = tk.Tk()
    window7.title("Consultar Alunos, Disciplinas e Professores por Curso")

    lbl_curso = tk.Label(window7, text="Selecione o ID do Curso:")
    lbl_curso.grid(row=0, column=0, padx=10, pady=5)

    combo_cursos = ttk.Combobox(window7, width=30)
    combo_cursos.grid(row=0, column=1, padx=10, pady=5)

    conexao = sqlite3.connect('RadCadastro.db')
    cur = conexao.cursor()
    cur.execute("SELECT cursoID FROM Curso")
    cursos = cur.fetchall()
    cursos_ids = [curso[0] for curso in cursos]
    combo_cursos['values'] = cursos_ids
    cur.close()
    conexao.close()

    btn_mostrar_alunos = tk.Button(window7, text="Mostrar Alunos", command=mostrar_alunos)
    btn_mostrar_alunos.grid(row=1, column=0, padx=10, pady=5)

    btn_mostrar_disciplinas = tk.Button(window7, text="Mostrar Disciplinas", command=mostrar_disciplinas)
    btn_mostrar_disciplinas.grid(row=1, column=1, padx=10, pady=5)

    btn_mostrar_professores = tk.Button(window7, text="Mostrar Professores", command=mostrar_professores)
    btn_mostrar_professores.grid(row=1, column=2, padx=10, pady=5)

    texto_alunos = tk.Text(window7, height=10, width=30)
    texto_alunos.grid(row=2, column=0, padx=10, pady=5)

    texto_disciplinas = tk.Text(window7, height=10, width=30)
    texto_disciplinas.grid(row=2, column=1, padx=10, pady=5)

    texto_professores = tk.Text(window7, height=10, width=30)
    texto_professores.grid(row=2, column=2, padx=10, pady=5)

    window7.mainloop()

import tkinter as tk
from tkinter import ttk
import sqlite3

def consultar_disciplina():
    def mostrar_alunos():
        disciplina_selecionada = combo_disciplinas.get()

        conexao = sqlite3.connect('RadCadastro.db')
        cur = conexao.cursor()

        cur.execute("SELECT Aluno.nomeAluno FROM Aluno INNER JOIN Curso ON Aluno.idCurso = Curso.cursoID INNER JOIN Disciplina ON Curso.cursoID = Disciplina.idCurso WHERE Disciplina.nomeDisciplina = ?", (disciplina_selecionada,))
        alunos = cur.fetchall()

        texto_alunos.delete(1.0, tk.END)

        if alunos:
            for aluno in alunos:
                texto_alunos.insert(tk.END, aluno[0] + "\n")
        else:
            texto_alunos.insert(tk.END, "Nenhum aluno matriculado nesta disciplina.")

        cur.close()
        conexao.close()

    def mostrar_professores():
        disciplina_selecionada = combo_disciplinas.get()

        conexao = sqlite3.connect('RadCadastro.db')
        cur = conexao.cursor()

        cur.execute("SELECT Professores.nomeProfessor FROM Professores INNER JOIN Disciplina ON Professores.idDisciplina = Disciplina.disciplinaID WHERE Disciplina.nomeDisciplina = ?", (disciplina_selecionada,))
        professores = cur.fetchall()

        texto_professores.delete(1.0, tk.END)

        if professores:
            for professor in professores:
                texto_professores.insert(tk.END, professor[0] + "\n")
        else:
            texto_professores.insert(tk.END, "Nenhum professor encontrado para esta disciplina.")

        cur.close()
        conexao.close()

    window8 = tk.Tk()
    window8.title("Consultar Alunos e Professores por Disciplina")

    lbl_disciplina = tk.Label(window8, text="Selecione a Disciplina:")
    lbl_disciplina.grid(row=0, column=0, padx=10, pady=5)

    combo_disciplinas = ttk.Combobox(window8, width=30)
    combo_disciplinas.grid(row=0, column=1, padx=10, pady=5)

    conexao = sqlite3.connect('RadCadastro.db')
    cur = conexao.cursor()
    cur.execute("SELECT nomeDisciplina FROM Disciplina")
    disciplinas = cur.fetchall()
    nomes_disciplinas = [disciplina[0] for disciplina in disciplinas]
    combo_disciplinas['values'] = nomes_disciplinas
    cur.close()
    conexao.close()

    btn_mostrar_alunos = tk.Button(window8, text="Mostrar Alunos", command=mostrar_alunos)
    btn_mostrar_alunos.grid(row=1, column=0, padx=10, pady=5)

    btn_mostrar_professores = tk.Button(window8, text="Mostrar Professores", command=mostrar_professores)
    btn_mostrar_professores.grid(row=1, column=1, padx=10, pady=5)

    texto_alunos = tk.Text(window8, height=10, width=50)
    texto_alunos.grid(row=2, column=0, padx=10, pady=5)

    texto_professores = tk.Text(window8, height=10, width=50)
    texto_professores.grid(row=2, column=1, padx=10, pady=5)

    window8.mainloop()


def tela_alunos():
    window2 = tk.Tk()

    window2.geometry("400x350")
    window2.title("Trabalho RAD")
    window2.resizable(False, False)

    nome_alunos_label = tk.Label(window2, text="Nome", font=("Arial", 10))
    nome_alunos_label.place(x=50, y=50)
    nome_aluno = tk.Entry(window2, width=40)
    nome_aluno.place(x=90, y=50)

    nota = tk.Entry(window2, width=40)
    nota.place(x=90, y=80)
    nota_label = tk.Label(window2, text="Nota", font=("Arial", 10))
    nota_label.place(x=50, y=80)

    id_curso_aluno = tk.Entry(window2, width=40)
    id_curso_aluno.place(x=90, y=110)
    id_curso_aluno_label = tk.Label(window2, text="Curso", font=("Arial", 10))
    id_curso_aluno_label.place(x=50, y=110)

    id_disc_aluno = tk.Entry(window2, width=40)
    id_disc_aluno.place(x=90, y=150)
    id_disc_aluno_label = tk.Label(window2, text="Disciplina", font=("Arial", 10))
    id_disc_aluno_label.place(x=20, y=150)

    botao_enviar_alunos = tk.Button(window2, text="Enviar", command=lambda: adicionar_aluno(nome_aluno.get(),nota.get(), id_curso_aluno.get(), id_disc_aluno.get()))
    botao_enviar_alunos.place(x=175, y=300)

    botao_deletar = tk.Button(window2, text="Deletar", command=lambda: del_aluno(nome_aluno.get()))
    botao_deletar.place(x=225, y=300)

    botao_update = tk.Button(window2, text="Update", command=lambda: upd_aluno(nome_aluno.get()))
    botao_update.place(x=275, y=300)

    window2.mainloop()

def tela_disciplina():
    window4 = tk.Tk()

    window4.geometry("400x350")
    window4.title("Trabalho RAD")
    window4.resizable(False, False)

    nome_disciplina_label = tk.Label(window4, text="Nome disciplina", font=("Arial", 10))
    nome_disciplina_label.place(x=1, y=50)
    nome_disciplina = tk.Entry(window4, width=40)
    nome_disciplina.place(x=100, y=50)

    id_curso_disc = tk.Entry(window4, width=40)
    id_curso_disc.place(x=90, y=110)
    id_curso_disc_label = tk.Label(window4, text="Curso id", font=("Arial", 10))
    id_curso_disc_label.place(x=50, y=110)

    botao_enviar_disciplina = tk.Button(window4, text="Enviar", command=lambda: adicionar_disciplina(nome_disciplina.get(), id_curso_disc.get()))
    botao_enviar_disciplina.place(x=175, y=300)

    botao_deletar2 = tk.Button(window4, text="Deletar", command=lambda: del_disciplina(nome_disciplina.get()))
    botao_deletar2.place(x=225, y=300)

    botao_update2 = tk.Button(window4, text="Update", command=lambda: upd_disciplina(nome_disciplina.get()))
    botao_update2.place(x=275, y=300)

    window4.mainloop()

def tela_curso():
    window5 = tk.Tk()

    window5.geometry("400x350")
    window5.title("Trabalho RAD")
    window5.resizable(False, False)

    nome_curso_label = tk.Label(window5, text="Nome Curso", font=("Arial", 10))
    nome_curso_label.place(x=20, y=50)
    nome_curso = tk.Entry(window5, width=40)
    nome_curso.place(x=100, y=50)

    botao_enviar_curso = tk.Button(window5, text="Enviar",command=lambda: adicionar_curso(nome_curso.get()))
    botao_enviar_curso.place(x=175, y=300)

    botao_deletar3 = tk.Button(window5, text="Deletar", command=lambda: del_curso(nome_curso.get()))
    botao_deletar3.place(x=225, y=300)

    botao_update3 = tk.Button(window5, text="Update", command=lambda: upd_curso(nome_curso.get()))
    botao_update3.place(x=275, y=300)

    window5.mainloop()

def tela_professores():
    window6 = tk.Tk()
    window6.geometry("400x350")
    window6.title("Trabalho RAD")
    window6.resizable(False, False)

    nome_professor_label = tk.Label(window6, text="Nome", font=("Arial", 10))
    nome_professor_label.place(x=50, y=50)
    nome_professor = tk.Entry(window6, width=40)
    nome_professor.place(x=90, y=50)

    id_disc_prof = tk.Entry(window6, width=40)
    id_disc_prof.place(x=90, y=110)
    id_disc_prof_label = tk.Label(window6, text="Disciplina id", font=("Arial", 10))
    id_disc_prof_label.place(x=1, y=110)

    id_curso_prof = tk.Entry(window6, width=40)
    id_curso_prof.place(x=90, y=150)
    id_curso_prof_label = tk.Label(window6, text="Curso id", font=("Arial", 10))
    id_curso_prof_label.place(x=1, y=150)

    botao_enviar_professor = tk.Button(window6, text="Enviar", command=lambda: adicionar_professor(nome_professor.get(), id_disc_prof.get(), id_curso_prof.get()))
    botao_enviar_professor.place(x=175, y=300)

    botao_deletar4 = tk.Button(window6, text="Deletar", command=lambda: del_professor(nome_professor.get()))
    botao_deletar4.place(x=225, y=300)

    botao_update4 = tk.Button(window6, text="Update", command=lambda: upd_professor(nome_professor.get()))
    botao_update4.place(x=275, y=300)

    window6.mainloop()

def visualizar_dados():
    window3 = tk.Tk()

    window3.geometry("400x350")
    window3.title("Trabalho RAD")
    window3.resizable(False, False)

    tabControl = ttk.Notebook(window3)

    tab1 = tk.Frame(tabControl)
    tab2 = tk.Frame(tabControl)
    tab3 = tk.Frame(tabControl)
    tab4 = tk.Frame(tabControl)
    tab5 = tk.Frame(tabControl)

    tabControl.add(tab1, text='Alunos')
    tabControl.add(tab2, text='Disciplinas')
    tabControl.add(tab3, text='Cursos')
    tabControl.add(tab4, text='Professor')
    tabControl.add(tab5, text='Gráfico')

    tree = ttk.Treeview(tab1, column=("c1", "c2", "c3"), show='headings')
    tree.column("#1", anchor=tk.CENTER, width=100)
    tree.heading("#1", text="MATRICULA")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="NOME")
    tree.column("#3", anchor=tk.CENTER, width=70)
    tree.heading("#3", text="NOTA")
    tree.pack(pady=20)

    tree2 = ttk.Treeview(tab2, column=("c1", "c2"), show='headings')
    tree2.column("#1", anchor=tk.CENTER, width=50)
    tree2.heading("#1", text="ID")
    tree2.column("#2", anchor=tk.CENTER, width=120)
    tree2.heading("#2", text="NOME DISCIPLINA")
    tree2.pack(pady=20)

    tree3 = ttk.Treeview(tab3, column=("c1", "c2"), show='headings')
    tree3.column("#1", anchor=tk.CENTER, width=50)
    tree3.heading("#1", text="ID")
    tree3.column("#2", anchor=tk.CENTER, width=120)
    tree3.heading("#2", text="NOME CURSO")
    tree3.pack(pady=20)

    tree4 = ttk.Treeview(tab4, column=("c1", "c2"), show='headings')
    tree4.column("#1", anchor=tk.CENTER, width=100)
    tree4.heading("#1", text="MATRICULA")
    tree4.column("#2", anchor=tk.CENTER, width=135)
    tree4.heading("#2", text="NOME PROFESSOR")
    tree4.pack(pady=20)

    #canvas = ttk.Canvas(tab5)

    con = sqlite3.connect('RadCadastro.db')
    c = con.cursor()
    c.execute("SELECT * FROM Aluno")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    c.execute("SELECT * FROM Disciplina")
    rows2 = c.fetchall()
    for row2 in rows2:
        tree2.insert("", tk.END, values=row2)
    c.execute("SELECT * FROM Curso")
    rows3 = c.fetchall()
    for row3 in rows3:
        tree3.insert("", tk.END, values=row3)
    c.execute("SELECT * FROM Professores")
    rows4 = c.fetchall()
    for row4 in rows4:
        tree4.insert("", tk.END, values=row4)
    con.close()

    tabControl.pack(expand=1, fill="both")

    window3.mainloop()

#conexao()
window = tk.Tk()
window.geometry("350x500")
window.title("Trabalho RAD")
window.resizable(False, False)

label = tk.Label(window, text="Cadastro Escola", font=("Arial", 15))
label.pack(pady=15)

botao1 = tk.Button(window, text="Alunos", width=20, height=2, command=tela_alunos)
botao1.pack(pady=10)

botao2 = tk.Button(window, text="Disciplinas", width=20, height=2, command=tela_disciplina)
botao2.pack(pady=10)

botao3 = tk.Button(window, text="Cursos", width=20, height=2, command=tela_curso)
botao3.pack(pady=10)

botao3 = tk.Button(window, text="Professores", width=20, height=2, command=tela_professores)
botao3.pack(pady=10)

botao4 = tk.Button(window, text="Visualização", width=20, height=2, command=visualizar_dados)
botao4.pack(pady=10)

botao5 = tk.Button(window, text="Visualização 2", width=20, height=2, command=consultar_curso)
botao5.pack(pady=10)

botao6 = tk.Button(window, text="Visualização 3", width=20, height=2, command=consultar_disciplina)
botao6.pack(pady=10)

window.mainloop()

