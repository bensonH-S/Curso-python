import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Configuração da conexão com o banco de dados
DATABASE_URI = 'mariadb+mariadbconnector://root:@localhost:3306/gecaf'
engine = create_engine(DATABASE_URI)

# Caminho do arquivo Excel e nome da aba
file_path = r"C:\Users\u512228\Documents\Base\Dados_CNP.xlsx"
sheet_name = "CNPS"

# Ler o Excel (a primeira linha é o cabeçalho e os dados começam na segunda linha)
df = pd.read_excel(file_path, sheet_name=sheet_name, header=0)

# Renomear as colunas para corresponder à tabela do banco de dados
df = df.rename(columns={
    "CNP": "cnp",
    "Situação": "situacao",
    "CNPJ": "cnpj",
    "Razão Social": "razao_social",
    "CC": "cc",
    "Telefone": "telefone",
    "Telefone do Proprietário": "telefone_proprietario",
    "Email": "email",
    "Endereço": "endereco",
    "Bairro": "bairro",
    "Cidade": "cidade",
    "UF": "uf",
    "CEP": "cep",
    "Latitude": "latitude",
    "Longitude": "longitude",
    "Inscrição Estadual": "inscricao_estadual"
})

# Função para converter coordenadas:
# Remove os pontos e divide por 1e6 para obter o valor decimal correto.
def convert_coord(val):
    try:
        s = str(val)
        s_clean = s.replace('.', '')
        return float(s_clean) / 1e6
    except Exception:
        return np.nan

# Aplicar a conversão nas colunas de latitude e longitude
df['latitude'] = df['latitude'].apply(convert_coord)
df['longitude'] = df['longitude'].apply(convert_coord)

# Limpar a coluna "inscricao_estadual" removendo todos os caracteres que não sejam dígitos
df['inscricao_estadual'] = df['inscricao_estadual'].astype(str).str.replace(r'\D', '', regex=True)

# Inserir os dados na tabela 'cnp_data' (append sem sobrescrever registros existentes)
df.to_sql('cnp_data', engine, if_exists='append', index=False)

print("Dados importados com sucesso!")
