import sqlite3
import datetime
from sqlite3.dbapi2 import Cursor
import os
import matplotlib.pyplot as plot


def conexao(db):
    conn = sqlite3.connect(db)
    return conn


def cur(conn):
    return conn.cursor()

def create_table(cursor):
    return cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
        id integer primary key autoincrement not null,
        date timestamp,
        prod_name TEXT,
        valor REAL
    )""")

def insert(data, prod_name, valor):
    sql_insert = f"INSERT INTO produtos (date, prod_name, valor) VALUES"
    sql_insert += f" ('{data}', '{prod_name}', '{valor}')"

    conn = conexao("dsa.db")
    cursor = cur(conn)

    cursor.execute(sql_insert)

    conn.commit()
    cursor.close()
    conn.close()


def update(data, prod_name, valor, id):
    sql_update = f"UPDATE produtos SET "
    sql_update += f"date='{data}', prod_name='{prod_name}', valor='{valor}' WHERE id={id}"

    conn = conexao("dsa.db")
    cursor = cur(conn)

    cursor.execute(sql_update)

    conn.commit()
    cursor.close()
    conn.close()

def delete(id):
    sql_delete = "DELETE from produtos"
    sql_delete += f" WHERE id='{id}'"

    conn = conexao("dsa.db")
    cursor = cur(conn)

    cursor.execute(sql_delete)

    conn.commit()
    cursor.close()
    conn.close()


def select():
    sql_select = "SELECT * FROM produtos"

    conn = conexao("dsa.db")
    cursor = cur(conn)

    cursor.execute(sql_select)

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados

def selectUM(id):
    sql_select = "SELECT * FROM produtos"
    sql_select += f" WHERE id = '{id}'"

    conn = conexao("dsa.db")
    cursor = cur(conn)

    cursor.execute(sql_select)

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados


def plottaGrafico():
    conn = conexao("dsa.db")
    cursor = cur(conn)

    cursor.execute("SELECT id, valor FROM produtos")

    ids = []
    valores = []
    dados = cursor.fetchall()

    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])
    
    plot.bar(ids, valores)
    plot.show()


# Cria uma conexao, insere esta conexão dentro do cursor, insere o cursor dentro do create table
# Gera uma tabela
create_table(cur(conexao("dsa.db")))



while True:
    print("-=-=-=-= SQLite3 - Criação de DB's -=-=-=-=")
    print("01. Insert")
    print("02. Update")
    print("03. Delete")
    print("04. Select")
    print("05. Plottar Gráfico")
    print("06 - Sair")

    opcao = input("Opção: 1-2-3-4-5-6 : ")
    os.system("clear")

    if opcao == "1":
        print("-=-= Inserção de dados -=-=")
        prod_name = input("Digite o nome do produto: ")
        valor = input("Digite o valor do produto: ")

        if prod_name and valor.isnumeric():
            valor = float(valor)

            insert(datetime.datetime.now(), prod_name, valor)
        
        else:
            print("Dados inválidos.")


    elif opcao == "2":
        print("-=-= Atualização de dados -=-=")
        prod_name = input("Digite o nome do produto: ")
        valor = input("Digite o valor do produto: ")
        id = input("Digite o ID: ")

        if prod_name and valor.isnumeric() and id.isnumeric():
            valor = float(valor)
            id = int(id)

            update(datetime.datetime.now(), prod_name, valor, id)

    elif opcao == "3":
        print("-=-= DELETAR registro -=-=")
        id = input("Digite o id: ")

        if id and id.isnumeric():
            existe = selectUM(id)
            if existe:
                delete(id)
                
                lista = select()

                for linha in lista:
                    print(f"ID: {linha[0]:<5} Data: {linha[1]:<40} Nome: {linha[2]} Valor (R$): {linha[3]:.2f}")
            else:
                print("ID inexistente na base de dados")

    elif opcao == "4":
        print("-=-= Listar todos os registros -=-=")
        
        lista = select()

        for linha in lista:
            print(f"ID: {linha[0]:<5} Data: {linha[1]:<40} Nome: {linha[2]:<40} Valor (R$): {linha[3]:.2f}")
    
    elif opcao == "5":
        print("-=-= Plottando Gráfico com Matplotlib")
        plottaGrafico()

    else:
        print("Saindo do programa")
        break
