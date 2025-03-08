from sqlalchemy import create_engine, text

print("Starting applications")

try:
    # Criando conexão com SQLAlchemy
    engine = create_engine("mysql+pymysql://root:@localhost/treinamento")
    connection = engine.connect()

    # Usando 'with' para gerenciar a conexão automaticamente
    with engine.connect() as connection:
        # Executando a query
        idade_minima = int(input("Digite a idade mínima: ")) # Recebe a idade do usuário
        result = connection.execute(text("SELECT * FROM pessoa WHERE idade > :idade" ), {"idade": idade_minima})
        
        # Converter os resultados em uma lista
        data = result.fetchall()
        
        # Verificando se há registros
        if not data:
            print("Não existe dados na tabela do banco")

        else:
            # Exibindo os resultados formatados
            print("\n🔹 Lista de Pessoas 🔹")
            for row in data:
                print(f"ID: {row[0]}, Nome: {row[1]}, Idade: {row[2]}, Profissão: {row[3]}, Cidade: {row[4]}")


except Exception as e:
    print(f"Erro ao conectar ao banco de dados {e}")
