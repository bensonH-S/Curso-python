'''Esse script scannear as porta aberta no servidor e gera um log'''

import socket
import datetime

def verificar_porta(host, porta):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Tempo limite de 1 segundo
            if s.connect_ex((host, porta)) == 0:
                return f"Porta {porta} está aberta."
            else:
                return f"Porta {porta} está fechada."
    except Exception as e:
        return f"Erro ao verificar porta {porta}: {e}"

def main():
    host = "10.90.7.1"  # Substitua pelo endereço IP do servidor
    portas = [3306, 5432, 22, 9100]  # Liste as portas relevantes
    log_filename = "resultado_portas.txt"

    with open(log_filename, "w") as log_file:
        log_file.write(f"Log de Verificação de Portas - {datetime.datetime.now()}\n")
        log_file.write("=" * 50 + "\n")
        
        for porta in portas:
            resultado = verificar_porta(host, porta)
            log_file.write(resultado + "\n")
        
        log_file.write("=" * 50 + "\n")
        log_file.write("Verificação concluída.\n")
    
    print(f"Resultado salvo em {log_filename}")

if __name__ == "__main__":
    main()

# pyinstaller --onefile result_doors.py
