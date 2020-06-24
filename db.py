import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

def criar_tabelas():
    cursor.execute("""
    create table desafios(
        id integer NOT NULL AUTO INCREMENT PRIMARY KEY,
        link_imagem text NOT NULL,
        nome_desafio text NOT NULL,
        resposta text NOT NULL, 
    )
    """)
    cursor.execute("""
    create table finalistas(
        id integer NOT NULL AUTO INCREMENT PRIMARY KEY,
        nick text NOT NULL,
        data date NOT NULL,
        mensagem text NOT NULL
    )
    """)

def novo_desafio(lista):
    cursor.execute("""
    insert into desafios(nome_desafio, resposta, link_imagem)
    values (?,?,?)
    """, lista)

def novo_finalista(lista):
    cursor.execute("""
    insert into finalistas(nick, data, mensagem)
    values(?,?,?)
    """,lista)