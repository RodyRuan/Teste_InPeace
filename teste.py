import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Derlomel0',
    database='teste',
)

cursor = conexao.cursor()


def cadastro_igreja_no_banco(Nome, Endereco, Website):
    import mysql.connector
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Derlomel0',
        database='teste',
    )

    cursor = conexao.cursor()
    comando = f'INSERT INTO info_igreja (Nome, Endereco, Website) VALUES ("{Nome}", "{Endereco}", "{Website}")'
    cursor.execute(comando)
    conexao.commit()


def cadastro_membro_no_banco(Nome_Membro, CPF, Data_Nascimento, Email, Telefone, Logradouro, Cidade, Estado, Nome_sua_igreja):
    import mysql.connector
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Derlomel0',
        database='teste',
    )

    cursor = conexao.cursor()
    executavel = f'INSERT INTO info_membro (Nome_Membro, CPF, Data_Nascimento, Email, Telefone, Logradouro, Cidade, Estado, Nome_sua_igreja) VALUES ("{Nome_Membro}", "{CPF}", "{Data_Nascimento}", "{Email}", "{Telefone}", "{Logradouro}", "{Cidade}", "{Estado}", "{Nome_sua_igreja}")'
    cursor.execute(executavel)
    conexao.commit()


def visualiza_membro(lista_de_membros):
    import mysql.connector
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Derlomel0',
        database='teste',
    )

    cursor = conexao.cursor()
    for _, Nome_Membro, CPF, Data_Nascimento, Email, Telefone, Logradouro, Cidade, Estado, Nome_sua_igreja in lista_de_membros:
        print(
            f"Nome: {Nome_Membro}, CPF: {CPF}, Email: {Email}, Telefone: {Telefone}, Logradouro: {Logradouro}, Cidade: {Cidade}, Estado: {Estado}, Nome da igreja pertencente: {Nome_sua_igreja}")


def edita(lista, lista_2, CPF_Para_Modificar, Nome_Membro_Novo, CPF_Novo, Data_Nascimento_Nova, Email_Novo,
          Telefone_Novo, Logradouro_Novo, Cidade_Nova, Estado_Novo, Nome_sua_igreja_Novo):
    import mysql.connector
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Derlomel0',
        database='teste',
    )

    cursor = conexao.cursor()
    lista_2 = []

    for id, Nome_Membro, CPF, Data_Nascimento, Email, Telefone, Logradouro, Cidade, Estado, Nome_sua_igreja in lista:
        lista_2.append([id, Nome_Membro, CPF, Data_Nascimento, Email, Telefone, Logradouro, Cidade, Estado,
                        Nome_sua_igreja])  # Precisei transformar em lista de lista para editar os componentes, já que tupla não pode ser modificada

    for id, _, CPF_lista_2, _, _, _, _, _, _, _ in lista_2:
        if CPF_Para_Modificar == CPF_lista_2:
            comando = f'UPDATE info_membro SET Nome_Membro = "{Nome_Membro_Novo}", CPF = "{CPF_Novo}", Data_Nascimento = "{Data_Nascimento_Nova}",Email = "{Email_Novo}", Telefone = "{Telefone_Novo}", Logradouro = "{Logradouro_Novo}", Cidade = "{Cidade_Nova}", Estado = "{Estado_Novo}", Nome_sua_igreja ="{Nome_sua_igreja_Novo}" WHERE IdMembro = {id}'

            cursor.execute(comando)
            conexao.commit()


def deleta_item(lista, CPF):
    import mysql.connector
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Derlomel0',
        database='teste',
    )

    cursor = conexao.cursor()
    for id, _, CPF_Membro, _, _, _, _, _, _, _ in lista:
        if CPF == CPF_Membro:
            comando = f'DELETE FROM info_membro WHERE IdMembro = {id}'
            cursor.execute(comando)
            conexao.commit()


def main():
    cadastro_igreja = input("Deseja cadastrar uma nova igreja no banco de dados? ").strip().lower()
    while cadastro_igreja != "sim" and cadastro_igreja != "não":
        cadastro_igreja = input("Digite sim ou não para dar continuidade ao programa: ").strip().lower()
    if cadastro_igreja == "sim":
        Nome = input("Digite o nome da sua Igreja: ")
        Endereco = input("Digite o endereço da sua Igreja: ")
        Website = input("Digite o nome do site da sua igreja: ")
        cadastro_igreja_no_banco(Nome, Endereco, Website)


    cadastro_membro = input("Deseja se tornar um membro da igreja ? ").lower().strip()
    while cadastro_membro != "sim" and cadastro_membro != "não":
        cadastro_membro = input("Digite sim ou não para dar continuidade ao programa: ").strip().lower()
    if cadastro_membro == "sim":
        Nome_Membro = input("Digite seu nome: ")
        CPF = input("Digite seu CPF: ")
        Data_Nascimento = input("Digite sua data de nascimento: ")
        Email = input("Digite seu email: ")
        Telefone = input("Digite seu telefone: ")
        Logradouro = input("Digite seu logradouro: ")
        Cidade = input("Qual a sua cidade? ")
        Estado = input("Qual o seu Estado? ")
        Nome_sua_igreja = input("Qual o nome da sua Igreja? ")
        cadastro_membro_no_banco(Nome_Membro, CPF, Data_Nascimento, Email, Telefone, Logradouro, Cidade, Estado, Nome_sua_igreja)


    listagem_membros = input("Deseja visualizar os nomes dos membros cadastrados? ").strip().lower()
    while listagem_membros != "sim" and listagem_membros != "não":
        cadastro_membro = input("Digite sim ou não para dar continuidade ao programa: ").strip().lower()
    if listagem_membros == "sim":
        visualizador_de_membros = f'SELECT * FROM info_membro'
        cursor.execute(visualizador_de_membros)
        visualizador = cursor.fetchall()
        visualiza_membro(visualizador)

    edicao = input("Deseja editar alguma informação? ").lower().strip()
    while edicao != "sim" and edicao != "não":
        edicao = input("Digite sim ou não para dar continuidade ao programa: ").strip().lower()
    if edicao == "sim":
        visualizador_de_membros = f'SELECT * FROM info_membro'
        cursor.execute(visualizador_de_membros)
        visualizador = cursor.fetchall()
        lista_2 = []
        New_CPF = input("Digite o CPF da pessoa ao qual deseja modificar os dados: ")

        CPF_Novo = input("Digite seu novo CPF: ")
        Nome_Membro_Novo = input("Digite seu novo nome: ")
        Data_Nascimento_Nova = input("Digite a nova data de nascimento: ")
        Email_Novo = input("Digite seu novo email: ")
        Telefone_Novo = input("Digite seu novo telefone: ")
        Logradouro_Novo = input("Digite seu novo Logradouro: ")
        Cidade_Nova = input("Digite sua nova Cidade: ")
        Estado_Novo = input("Digite seu novo Estado: ")
        Nome_sua_igreja_Novo = input("Digite sua nova Igreja: ")
        edita(visualizador, lista_2, New_CPF, Nome_Membro_Novo, CPF_Novo, Data_Nascimento_Nova, Email_Novo,
              Telefone_Novo, Logradouro_Novo, Cidade_Nova, Estado_Novo, Nome_sua_igreja_Novo)

    deleta = input("Deseja deletar um membro? ").strip().lower()
    while deleta != "sim" and deleta != "não":
        deleta = input("Digite sim ou não para dar continuidade ao programa.").strip().lower()
    if deleta == "sim":
        info_para_deletar = input("Digite o CPF do membro que você deseja deletar: ")
        visualizador_de_membros = f'SELECT * FROM info_membro'
        cursor.execute(visualizador_de_membros)
        visualizador = cursor.fetchall()
        deleta_item(visualizador, info_para_deletar)


if __name__ == "__main__":
    main()
cursor.close()
conexao.close()
