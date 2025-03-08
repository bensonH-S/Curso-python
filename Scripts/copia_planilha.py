import shutil
import os
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QTimer

# Caminho do arquivo de origem
origem = r"C:\Users\u811737\OneDrive - BRB - Banco de Brasilia SA\Arquivos de Chat do Microsoft Teams\PAGAMENTOS DE AGÊNCIAS 2025-corrigido.xlsm"

# Caminho da pasta de destino
destino = r"W:\_GERAL\gecafpag\PAGAMENTOS DE AGÊNCIAS 2025-corrigido.xlsm"

def exibir_notificacao(mensagem):
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(mensagem)
    msg_box.setWindowTitle("Notificação")
    QTimer.singleShot(5000, msg_box.close)  # Fecha a mensagem após 5 segundos
    msg_box.show()
    app.exec_()

def copiar_arquivo():
    try:
        shutil.copy2(origem, destino)
        exibir_notificacao("Arquivo copiado com sucesso!")
    except FileNotFoundError:
        exibir_notificacao("Erro: Arquivo de origem não encontrado.")
    except PermissionError:
        exibir_notificacao("Erro: Permissão negada ao acessar o arquivo ou pasta.")
    except Exception as e:
        exibir_notificacao(f"Erro inesperado: {e}")

# Executa a cópia do arquivo
copiar_arquivo()
# pyinstaller --onefile --icon=copia.ico copia_planilha.py