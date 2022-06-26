clientes = []

resp = 'sim'
while resp == 'sim':
    clientes.append(input('\nDigite o nome completo: '))
    clientes.append(input('\nDigite o RG: '))
    clientes.append(input('\nDigite o CPF: '))
    clientes.append(input('\nDigite o telefone: '))
    resp = input('\nQuer cadastrar outro cliente (sim/não)? ')

n = 4
cliente = [clientes[i:i + n] for i in range(0, len(clientes), n)]
print(cliente)