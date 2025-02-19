# """
# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, +
# """
# #        +01234
# #        -54321
# string = 'ABCDE'  # 5 caracteres (len)
# # print(bool([]))  # falsy
# # print(lista, type(lista))

# #        0    1      2              3    4
# #       -5   -4     -3             -2   -1
# lista = [123, True, 'Luiz Otávio',  1.2, []]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))

print('-' *79)





# """
# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis:
#     append, insert, pop, del, clear, extend, +
# Create Read Update   Delete
# Criar, ler, alterar, apagar = lista[i] (CRUD)
# """
# #        0   1   2   3   4   5
# lista = [10, 20, 30, 40]
# # lista[2] = 300
# # del lista[2]
# # print(lista)
# # print(lista[2])
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3)
# print(lista, 'Removido,', ultimo_valor)

print('-' *79)





"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

print('-' *79)





# lista = [10, 20, 30, 40]
# lista.append('Henrique')
# lista.append(1234)
# print(lista)
# print(len(lista))
# del lista[5]
# print(lista)
# # lista.clear()
# lista.insert(0, 'inicio')
# print(lista)

print('-' *79)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b

print(lista_c)
lista_a.extend(lista_b)
print(lista_a)

print('-' *79)







