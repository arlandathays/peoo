lista = []
resp = 'sim'

while resp == 'sim':
    lista.append(int(input('\nDigite um numero: ')))
    resp = input('\nQuer digitar outro numero (sim/não)? ')

def crescente(lista):
    lista.sort()
    print(lista)

def decrescente(lista):
    lista.sort(reverse=True)
    print(lista)

def par(lista):
  for i in lista:
    if (i%2) == 0:
      print(i)
      
crescente(lista)
decrescente(lista)
par(lista)