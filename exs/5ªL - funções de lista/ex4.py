from functools import reduce

w = [3, 2, 5, 6, 2, 3, 5, 2]

def prod_lista(lista):
  return reduce(lambda x, y: x * y, lista)

print(prod_lista(w))
