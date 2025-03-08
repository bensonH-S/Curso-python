import os
import win32com.client as win32
import pdfkit
import ctypes

# Diretório para os arquivos .msg
msg_directory = r'Z:\\_ESTAGIARIO\\Correspondentes\\ADMINISTRATIVO\\Remessa de Documentos\\Notas Novembro_24\\Cobrança E-mails'

# Diretório para salvar os arquivos PDF
pdf_directory = r'Z:\\_ESTAGIARIO\\Correspondentes\\ADMINISTRATIVO\\Remessa de Documentos\\Notas Novembro_24\\Cobrança E-mails PDF'

# Função para converter .msg para .pdf
def converter_msg_para_pdf(msg_path, cnp):
    # Cria uma instância do Outlook
    outlook = win32.Dispatch('outlook.application')
    
    # Abre o arquivo .msg
    msg = outlook.CreateItemFromTemplate(msg_path)
    
    # Salva o e-mail como HTML
    html_path = os.path.join(msg_directory, f"{cnp}.html")
    msg.SaveAs(html_path, 5)  # 5 é o formato HTML
    
    # Converte o arquivo HTML para PDF usando pdfkit
    os.makedirs(pdf_directory, exist_ok=True)
    pdf_path = os.path.join(pdf_directory, f"{cnp}.pdf")
    
    try:
        pdfkit.from_file(html_path, pdf_path)
        print(f"Arquivo PDF gerado: {pdf_path}")
    except Exception as e:
        print(f"Erro ao converter para PDF: {e}")
    
    # Apaga o arquivo HTML temporário
    os.remove(html_path)

# Percorre todos os arquivos .msg na pasta
for filename in os.listdir(msg_directory):
    if filename.endswith(".msg"):
        msg_path = os.path.join(msg_directory, filename)
        cnp = os.path.splitext(filename)[0]  # Obtém o nome do arquivo sem a extensão .msg
        converter_msg_para_pdf(msg_path, cnp)

# Exibe uma mensagem pop-up informando que o processo foi concluído
ctypes.windll.user32.MessageBoxW(0, "Processo concluído. Arquivos .msg convertidos para PDF.", "Informação", 0x40 | 0x1)
