# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True 

senha_de_acesso = '12345'
senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')
elif senha == senha_de_acesso:
    print('Você entrou no sistema')
else:
    print('Senha errada')