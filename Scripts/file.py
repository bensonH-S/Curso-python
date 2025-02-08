import os

# Definir a estrutura das pastas
structure = {
    "Grupo_Alvimm": {
        "backend": {
            "app": ["models", "services", "utils", "api", "auth"],
            "config": [],
            "migrations": [],
            "requirements.txt": [],
            "main.py": []
        },
        "frontend": {
            "public": [],
            "src": ["components", "pages", "store", "styles", "App.vue"]
        },
        "tests": ["unit", "integration"],
        "scripts": [],
        "README.md": []
    }
}

# Função recursiva para criar as pastas
def create_structure(base_path, structure):
    for key, value in structure.items():
        # Caminho completo para a pasta ou arquivo
        current_path = os.path.join(base_path, key)
        
        # Verifica se é uma pasta ou um arquivo
        if isinstance(value, list):  # Se for lista, cria arquivos
            for item in value:
                file_path = os.path.join(current_path, item)
                # Cria o arquivo
                with open(file_path, 'w') as f:
                    pass
        elif isinstance(value, dict):  # Se for dicionário, cria pastas
            os.makedirs(current_path, exist_ok=True)
            create_structure(current_path, value)

# Caminho base para criar a estrutura
base_path = "Grupo_Alvim"

# Criação da estrutura
os.makedirs(base_path, exist_ok=True)
create_structure(base_path, structure)

print("Estrutura de pastas criada com sucesso!")
