# Aprendendo a calcular imc
# IMC = PESO / ALTURA²

nome = 'Henrique Silva'
altura = 1.75
valor = 1254
peso = 70
imc = peso / (altura ** 2)
print(nome, 'seu IMC é:', imc)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)

x = 10
y = 5

print(f'O resultado de {x} + {y} é {x + y}.\n')

''' FORMATANDO VALORES
 AS F-STRINGS TAMBÉM PERMITEM APLICAR FORMATOS ESPECIAIS DIRETAMENTE NOS VALORES DENTRO DE {}'''
 
valor = 1234.56789
print(f'O valor formatado é {valor:.2f}.\n')

'''AS F-STRINGS TAMBÉM PERMITEM APLICAR ALINHAMENTO E TEXTOS'''

texto = 'Python'

print(f'|{texto:^10}|\n'*2) # Centralizado
print(f'|{texto:<10}|\n'*2) # Alinhado à esquerda
print(f'|{texto:>10}|\n'*2) # Alinhado à direita

'''INSERIDO NÚMEROS COM ZEROS'''

numero = 42
print(f'O número é {numero:05}.') # 05  Adiciona zeros à esquerda, totalizando 5 caracteres. Saída: