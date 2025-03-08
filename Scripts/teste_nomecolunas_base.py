import pandas as pd

# Caminho para a planilha Excel
excel_path = r'Y:\\Correspondentes\\ADMINISTRATIVO\\Remessa de Documentos\\Notas Outubro_24\\Certidões\\teste.xlsm'

# Leitura da planilha Excel, considerando o cabeçalho na segunda linha (índice 1)
df = pd.read_excel(excel_path, sheet_name='CERTIDÕES', header=1)

# Lista os nomes das colunas
print("Nomes das colunas na planilha:")
print(df.columns)