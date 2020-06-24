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
        estado integer NOT NULL
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
    insert into desafios(nome_desafio, resposta, link_imagem, estado)
    values (?,?,?,?)
    """, lista)
    conn.close()

def deletar_desafios(id_desafio):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM desafios
    WHERE id = ?
    """,id_desafio)
    conn.commit()
    conn.close()

def atualizar_desafios(lista):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE desafios
    SET link_imagem = ?, nome_desafio = ?, resposta = ?
    WHERE id = ?
    """,lista)
    conn.close()

def buscar_desafio(id_desafio):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM desafios
    WHERE id = ?
    """,id_desafio)
    return cursor.fetchone()
    conn.close()

def atualizar_status(lista):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE desafios
    SET estado = ?
    WHERE id = ?
    """,lista)
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

