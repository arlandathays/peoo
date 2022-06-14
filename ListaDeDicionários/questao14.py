nome = str(input('Digite um nome: '))
name = {}

for i in nome:
    if i !=' ':
        name.update({i:nome.count(i)})
print(name)