lista = []
resp = 'sim'

while resp == 'sim':
    lista.append(input('\nDigite o nome: '))
    lista.append(int(input('\nDigite a idade: ')))
    resp = input('\nQuer digitar outro usuário (sim/não)? ')

def procurar(lista, busca):
  if busca in lista:
    posicao=lista.index(busca)
    lista.pop(posicao)
    lista.pop(posicao)
    print(lista)
  else:
    print(f'O nome "{busca}" não consta na lista.')

busca=input("Procure na lista: ")
procurar(lista, busca)