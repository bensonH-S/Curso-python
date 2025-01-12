import os
import sqlite3

# Caminho para a pasta com os bancos de dados
database_folder = r"F:\databases"
search_word = "banana"

def search_in_database(db_path, search_word):
    """
    Procura uma palavra específica em todas as tabelas de um banco de dados SQLite.
    """
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Lista as tabelas do banco de dados
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        print(f"Procurando em: {db_path}")
        
        for table_name, in tables:
            print(f"  Verificando tabela: {table_name}")
            try:
                # Busca a palavra em todas as colunas da tabela
                cursor.execute(f"PRAGMA table_info({table_name});")
                columns = [row[1] for row in cursor.fetchall()]
                
                for column in columns:
                    query = f"SELECT * FROM {table_name} WHERE {column} LIKE ?"
                    cursor.execute(query, (f"%{search_word}%",))
                    results = cursor.fetchall()
                    
                    if results:
                        print(f"    Palavra encontrada na tabela '{table_name}', coluna '{column}':")
                        for result in results:
                            print(f"      {result}")
            except Exception as e:
                print(f"    Erro ao verificar tabela '{table_name}': {e}")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados '{db_path}': {e}")
    finally:
        if connection:
            connection.close()

def main():
    """
    Percorre todos os bancos de dados na pasta e busca a palavra especificada.
    """
    for file_name in os.listdir(database_folder):
        if file_name.endswith(".db") or file_name.endswith(".sqlite"):
            db_path = os.path.join(database_folder, file_name)
            search_in_database(db_path, search_word)

if __name__ == "__main__":
    main()
