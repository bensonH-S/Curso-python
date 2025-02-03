import schedule
import time
import subprocess

# Função para rodar o script
def rodar_script():
    script_path = r"F:\Users\Administrador\OneDrive\Área de Trabalho\Automation System\KingManage\dbe.py"
    subprocess.run(["python", script_path])

# Agendar para rodar todos os dias às 21h10
schedule.every().day.at("22:23").do(rodar_script)

# Loop para verificar o agendamento
while True:
    schedule.run_pending()
    time.sleep(60)  # Espera um minuto antes de verificar novamente
