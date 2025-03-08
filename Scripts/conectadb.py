import mariadb
 
try:
    conn = mariadb.connect(
        host="localhost",
        user="root",
        password="",
        database="pessoas",
        port=3306
    )
    print(f"✅ Conexão bem-sucedida!")
    conn.close()
except mariadb.Error as err:
    print(f"❌ Erro ao conectar no banco de dados!")