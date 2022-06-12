vogais = {'e': 2, 'a': 1, 'u': 5, 'i': 3, 'o': 4}

for i in sorted(vogais):
    print('Ordem crescente:', i, vogais[i])
print('---------------')
for i in sorted(vogais, reverse=True):
    print('Ordem decrescente:', i, vogais[i])