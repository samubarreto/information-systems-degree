# map(função, iterável)
# map(oq fazer, alguma lista ou string)

lista = ['1', '3', '243']
print(lista)
lista = list(map(int, lista)) # n devolve uma lista, por isso do list()
print(lista)

# filter(condição, alguma lista ou string)
# lambda (recebe): (devolve)

valores = [-1, -34, 45, 345, 45, 2, -6]
print(list(filter(lambda x: x > 0, valores)))