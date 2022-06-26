num = []

resp = 'sim'
while resp == 'sim':
    num.append(int(input('\nDigite um número: ')))
    resp = input('\nQuer digitar outro número (sim/não)? ')

soma = sum(num)

print(num)
print(soma)