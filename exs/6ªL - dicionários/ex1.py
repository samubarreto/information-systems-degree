from random import randint

d = {1: 0,
      2: 0,
      3: 0,
      4: 0,
      5: 0,
      6: 0}

for _ in range(100):
  sorteio = randint(1, 6)
  d[sorteio] += 1

print(*d.items())
