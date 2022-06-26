num = []

resp = 'sim'
while resp == 'sim':
    num.append(int(input('\nDigite um número: ')))
    resp = input('\nQuer digitar outro número (sim/não)? ')
print(f'\nLista de Númeross: {num}')

num.sort()
print(f'O segundo maior número é: {num[-2]}')