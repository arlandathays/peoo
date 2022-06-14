pessoas = [{'nome': 'Maria', 'cidade': 'Belo Horizonte'}, {'nome': 'Maria', 'cidade': 'São Paulo'}, {'nome': 'Pedro', 'cidade': 'Curitiba'}]

nome=[]
cidade=[]

for i in pessoas:
    nome.append(i['nome'])
    cidade.append(i['cidade'])
print('nome=', nome)
print('cidade=', cidade)