import random

nomes = ['Ana', 'Jane', 'Maria', 'Bia', 'Mel', 'Clara']
def aleatorio(nomes):
  return random.choice(nomes)

print(aleatorio(nomes))