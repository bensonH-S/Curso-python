import win32com.client as win32

# Cria uma instância do Outlook
outlook = win32.Dispatch('outlook.application')

# Cria um novo e-mail
mail = outlook.CreateItem(0)

# Define a conta de envio
account = None
for acc in outlook.Session.Accounts:
    if acc.DisplayName == 'gecafnotas@brb.com.br':
        account = acc
        break

if account:
    mail._oleobj_.Invoke(*(64209, 0, 8, 0, account))  # Define a conta de envio
    mail.To = 'estagiariosgecaf@estagiarios.brb.com.br'
    mail.Subject = 'Teste'
    mail.Body = 'testando o email, enviado pelo script python'
    mail.Send()
    print("E-mail enviado com sucesso!")
else:
    print("Conta 'gecafnotas' não encontrada.")
