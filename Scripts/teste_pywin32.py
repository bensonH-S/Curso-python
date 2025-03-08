# Esse Script verificar se a biblioteca pywin32 foi instalada correta

import win32com.client

try:
    outlook = win32com.client.Dispatch('outlook.application')
    print("Biblioteca pywin32 instalada e funcionando corretamente!")
except Exception as e:
    print(f"Erro ao testar a biblioteca: {e}")


# Verificando quais são os emails configurado no outlook

import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

for acc in outlook.Session.Accounts:
    print(acc.DisplayName)
