import sqlite3
import os

# Remove o arquivo com o DB SQLite caso ele exista
#os.remove("escola.db") if os.path.exists("escola.db") else None

# Criando conexão com o banco de dados
# Se caso o DB não existir, ele será criado.
conn = sqlite3.connect("escola.db")

# Verificando o tipo de arquivo
print(type(conn))

# Criando um cursor, isso vai permitir percorrer todos os registros em um conjunto de dados
cur = conn.cursor()

# Verificando tipo de arquivo cursor
print(type(cur))

# Criando comando SQL para criação da tabela cursos
sql = """ create table if not exists cursos (
            id integer primary key AUTOINCREMENT,
            titulo varchar(100),
            categoria varchar(140)
            );
        """

# executando a instrução sql do cursor
cur.execute(sql)


# Inserir registro no DB


while True:
    print("Inserção de Cursos em Banco de Dados SQLite3")
    print("1. Inserir Registros")
    print("2. Listar Registros")
    print("3. Sair")

    opcao = input("Opção 1-2-3 : ")
    os.system("clear")

    if opcao and opcao.isnumeric():
        if opcao == "1":

            conta = 0
            sql_insert = """insert into cursos (titulo, categoria) VALUES"""

            while True:
                titulo = input("Digite o título do curso: ")
                categoria = input("Digite a categoria: ")

                if titulo and categoria:
                    if conta < 1:
                        sql_insert += f" ('{titulo}', '{categoria}') "
                        conta += 5
                    else:
                        sql_insert += ","
                        sql_insert += f"('{titulo}', '{categoria}') "

                    continua = input("Deseja inserir mais um título? s ou n : ")

                    if continua in "sS":
                        continue
                    else:
                        # criando laço for para inserir lista no DB
                        cur.execute(sql_insert)

                        # grava transação
                        conn.commit()
                        break
                    
                else:
                    print("É preciso preencher ambos os campos para inserir no DB.")
        elif opcao == "2":
            print("Listando registros: ")

            # Fazendo uma query SELECT
            sql_select = "select * from cursos"

            # seleciona todos os registro e os recupera
            cur.execute(sql_select)

            dados = cur.fetchall()

            for linha in dados:
                print(f"ID: {linha[0]} Título: {linha[1]} Categoria: {linha[2]}")


        elif opcao == "3":
            print("Encerrando o programa")
            break

        else:
            print("Opção inexistente.")
    
    else:
        print("Opção inválida")

#print(sql_insert)







