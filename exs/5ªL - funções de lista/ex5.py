def media_digitos(n):
    digitos = [int(d) for d in str(n)]
    return sum(digitos) / len(digitos)

print(media_digitos(727))