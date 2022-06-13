lista = {}
compras = ['Laranja','Manga','Arroz','Macarrão']
quantidade=[10.00, 3.00, 2.00, 3.0]

for i in range(len(compras)):
    lista.update({compras[i]: quantidade[i]})
print(lista)

for i in range(len(compras)):
    lista.update({compras[i]: quantidade[i]*3})
print(lista)