# # INTERPOLAÇÃO DE STRING (% - MÉTODO ANTIGO)
# nome = "Carlos"
# mensagem = "Olá, %s ! Bem-vindo ao curso." %nome
# print(mensagem)
# print(40 * "=")

# # MÉTODO .format()
# nome = "Carlos"
# idade = 30
# mensagem = "Olá meu nome é {} e tenho {} anos.".format(nome,idade)
# print(mensagem)
# print(40 * "=")

# # F-STRINGS (INTERPOLAÇÃO MODERNA)
# nome = "Carlos"
# idade = 25
# mensagem = f"Meu nome é {nome} e tenho {idade} anos."
# print(mensagem)
# print(40 * "=")

'''A TIVIDADE DE FORMATAÇAÕ DE STRING'''

# Interpolação com métodologia antiga
nome = "Lucas"
idade = 30
salario = 2500.75

mensagem = "Meu nome é %s tenho %d anos e ganho R$ %f por mês." %(nome, idade, salario)
print(mensagem)
print(40 * "=")


# Utilizando .format()
produto = "Notebook"
preco = 4500.99
quantidade = 3

mensagem = "O produto {} custa R$ {} e temos {} unidade em estoque.".format(produto, preco, quantidade)
print(mensagem)
print(40 * "=")


# Utilizando f-strings
cidade = "São paulo"
temperatura = 28.5

mensagem = f"Hoje em {cidade} a temperatura é de {temperatura} graus."
print(mensagem)


pi = 3.1415926535
mensagem = f"O valor de PI com duas casas decimais é {pi:.2F}"
print(mensagem)