lista={}
nome = []
idade = []

resp = 'sim'
while resp == 'sim':
    nome.append(input('\nDigite o nome: '))
    idade.append(int(input('\nDigite a idade: ')))
    resp = input('\nQuer digitar outro usuário (sim/não)? ')

for i in range(len(nome)):
    lista.update({nome[i]: idade[i]})
print(lista)

def procurar(lista, busca):
  if busca in lista:
    del lista[busca]
    print(lista)
  else:
    print(f'O nome "{busca}" não consta na lista.')

busca=input("Procure na lista: ")
procurar(lista, busca)