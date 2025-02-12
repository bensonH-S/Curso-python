"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    num = int(input("Por gentileza, digite um número inteiro: "))
    result = num % 2

    if result == 0:
        print("O número que você digitou é um número par")
    elif result == 1:
        print("O número que você digitou é ímpar")
except:
    print("Você não digitou um número inteiro")   

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = float(input("Olá, que horas são? "))

if horas >= 0 and  horas <= 11:
    print(f"Bom dia! ")
if horas >= 12 and horas <= 17:
    print(f"Boa tarde! ")
if horas >= 18 and horas <= 23:
    print(f"Boa noite! ")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Olá, digite seu primeiro nome: ")

if len(nome) <= 4:
    print('seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('seu nome é normal')
else:
    print('Seu nome é grande')