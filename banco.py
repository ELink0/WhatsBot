import sqlite3

conexao = sqlite3.connect("./src/banco/medicamentos.sqlite")

def criar_tabela(conexao):
    cursor = conexao.cursor()
    
    sql = """
    CREATE TABLE IF NOT EXISTS medicamentos(
        nome TEXT,
        qtd_estoque INT,
        preco FLOAT
    );
    """
    cursor.execute(sql)

def inserir_medicamento(conexao, nome, qtd_estoque, preco):
    cursor = conexao.cursor()

    sql = """
    INSERT INTO medicamentos VALUES(
        '{}',
        '{}',
        '{}'
    );\n
    """.format(nome, qtd_estoque, preco)
    cursor.execute(sql)
    conexao.commit()


def listar_medicamentos(conexao):
    cursor = conexao.cursor()

    sql = "SELECT rowid, * FROM medicamentos;"
    cursor.execute(sql) 

    lista_medicamentos = cursor.fetchall()
    
    for u in medicamentos:
        print("ID: {} - Nome: {} ".format(u[0], u[1]))
    print("\n\n")
