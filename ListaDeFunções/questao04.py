dicionario={}
item = []
valor = []

resp = 'sim'
while resp == 'sim':
    item.append(input('\nDigite o item: '))
    valor.append(int(input('\nDigite um número: ')))
    resp = input('\nQuer adicionar outro item (sim/não)? ')

for i in range(len(item)):
    dicionario.update({item[i]: valor[i]})
print(dicionario)

mult = int(input('Por quanto deseja multiplicar? '))

for i in range(len(item)):
    dicionario.update({item[i]: valor[i]*mult})
print(dicionario)