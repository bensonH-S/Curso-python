# Verificando se a biblioteca pandas foi instalada corretamente.

import pandas as pd

try:
    # Cria um DataFrame de exemplo
    df = pd.DataFrame({'coluna1': [1, 2], 'coluna2': [3, 4]})
    print("Biblioteca pandas instalada e funcionando corretamente!")
    print(df)
except Exception as e:
    print(f"Erro ao testar a biblioteca: {e}")
