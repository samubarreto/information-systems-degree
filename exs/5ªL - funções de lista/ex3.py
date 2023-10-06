w = [3, 2, 5, 6, 2, 3, 5]

def indices_pares(w):
    return list(map(lambda i: w[i], range(0, len(w), 2)))

print(indices_pares(w))