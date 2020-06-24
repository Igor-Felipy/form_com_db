import sqlite3

def criar_tabelas():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
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
    conn.close()

def novo_desafio(lista):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
    insert into desafios(nome_desafio, resposta, link_imagem)
    values (?,?,?)
    """, lista)
    conn.close()


def novo_finalista(lista):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
    insert into finalistas(nick, data, mensagem)
    values(?,?,?)
    """,lista)
    conn.close()


def consultar_finalistas():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM finalistas;
    """)
    return cursor.fetchall()
    conn.close()
