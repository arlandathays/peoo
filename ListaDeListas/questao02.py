nomes = []

resp = 'sim'
while resp == 'sim':
    nomes.append(input('\nDigite um nome: '))
    resp = input('\nQuer digitar outro nome (sim/não)? ')
print(f'\nLista de Nomes: {nomes}')

for i in range(len(nomes)):
    print(nomes[i])
resp = 'sim'
while resp =='sim':
    pesq = input('\nQual nome deseja procurar? ')
    if pesq in nomes:
        print(f'\nO nome solicitado foi {pesq} e sua posição na lista é {nomes.index(pesq)}.')
    else:
        print(f'\nO nome {pesq} não consta na lista.')
    resp = input('\nDeseja pesquisar outro nome (sim/não)? ')

del nomes[0]
nomes.insert(0, pesq)
print(f'\nLista com nome substituido: ')
for i in range(len(nomes)):
    print(nomes[i])

nomes.sort()
print(f'\nLista em ordem alfabética: ')
for i in range(len(nomes)):
    print(nomes[i])

nomes.pop()
print(f'\nLista com o primeiro elemento deletado: ')
for i in range(len(nomes)):
    print(nomes[i])

nomes.pop(0)
print(f'\nLista com o último elemento deletado: ')
for i in range(len(nomes)):
    print(nomes[i])
