a = 'A'
b = 'B'
c = 1.1

string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b ,nome3=c)

print(formato)

# Exemplos Básicos
# 1. Inserindo Valores

nome = "Maria"
idade = 30
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))

# 2. Usando Índices
print("Meu nome é {0} e eu tenho {1} anos.".format("João", 25))
print("Eu inverti: {1} e {0}.".format("João", 25))

# 3. Usando Nomes
print("Meu nome é {nome} e eu tenho {idade} anos.".format(nome="Ana", idade=28))



# Formatações Avançadas
# 1. Casas Decimais

valor = 123.45678
print("O valor formatado é {:.2f}.".format(valor))

# 2. Alinhamento de Textos
texto = "Python"
print("|{:^10}|".format(texto))  # Centralizado
print("|{:<10}|".format(texto))  # Alinhado à esquerda
print("|{:>10}|".format(texto))  # Alinhado à direita