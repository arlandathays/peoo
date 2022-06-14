d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
geral = [d1, d2]
contador = {}

for i in geral:
    for x in i.keys():
        if x not in contador:
            contador.update({x: i[x]})
        else:
            contador[x] = d1[x]+d2[x]

print(f'contador {contador}')