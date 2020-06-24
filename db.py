import sqlite3

conn = sqlite3.connect('form_com_db/clientes.db')

cursor = conn.cursor()

def criar_banco():
    cursor.execute("""
    create table clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
    );
    """)

    print('Tabela ciada com sucesso.')
    conn.close()

def registrar_teste():
    cursor.execute("""
    insert into clientes (nome,idade,cpf,email,fone,cidade,uf,criado_em)
    values ('Regis','35','00000000000','regis@email.com','11-987654321','São Paulo','SP','2014-06-08')
    """)
    cursor.execute("""
    insert into clientes (nome,idade,cpf,email,fone,cidade,uf,criado_em)
    values ('Aloisio','87','11111111111','aloisio@email.com','98765-4322','Porto Alegre','RS','2014-06-09')
    """)
    cursor.execute("""
    insert into clientes (nome,idade,cpf,email,fone,cidade,uf,criado_em)
    values ('Bruna','21','22222222222','bruna@email.com','21-98765-4323','Rio de Janeiro','RJ','2014-06-09')
    """)

    cursor.execute("""
    insert into clientes (nome,idade,cpf,email,fone,cidade,uf,criado_em)
    values ('Matheus','19','33333333333','matheus@email.com','11-98765-4324','Campinas','SP','2014-06-08')
    """)

    conn.commit()
    print('Dados Inseridos com sucesso')
    conn.close()


