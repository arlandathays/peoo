lista={}
resp = 'sim'

nome = []
telefone = []

while resp == 'sim':
    nome.append(input('\nDigite o nome: '))
    telefone.append(int(input('\nDigite o telefone: ')))
    resp = input('\nQuer digitar outro contato (sim/não)? ')

for i in range(len(nome)):
    lista.update({nome[i]: telefone[i]})
print(lista)