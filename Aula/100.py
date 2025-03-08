# # Desafio 1: Contagem Regressiva (while)

num = int(input('Digite um número: '))

while num >= 0:
    
    print(num)
    num -= 1
    
print('FIM')

# Desafio 2: Tabuada (for)

num = int(input('Digite um número: '))

for i in range(1, 11): # Vai de 1 até 10
    print(f'{num} * {i} =', num*i)

#  3: Soma de Números Positivos (while)

soma = 0

while True:
    num = int(input('Digite um número: '))

    if num < 0: 
        break
    
    soma += num

print(f'A soma dos número digitados é: {soma}')

# Desafio 4: Contador de Vogais (for)

frase = input('Digite uma frase: ').lower()  # Converte para minúsculas

vogais = 'aeiou'  # Conjunto de vogais
qtd_vogais = 0  # Inicializa o contador

for letra in frase:  # Percorre cada caractere da frase
    if letra in vogais:  # Se for vogal, aumenta o contador
        qtd_vogais += 1  

print(f'A frase tem {qtd_vogais} vogais.')  # Exibe o total de vogais
