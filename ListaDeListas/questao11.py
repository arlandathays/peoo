lista1 = []
resp = 'sim'
while resp == 'sim':
    lista1.append(input('\nDigite um elemento para a lista 1: '))
    resp = input('\nQuer digitar outro elemento para a lista 1(sim/não)? ')

lista2 = []
resp = 'sim'
while resp == 'sim':
    lista2.append(input('\nDigite um elemento para a lista 2: '))
    resp = input('\nQuer digitar outro elemento para a lista 2 (sim/não)? ')


print(lista1)
print(lista2)

for i in lista1:
  if i in lista2:
   print('True')