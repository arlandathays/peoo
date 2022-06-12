codigo = int(input('Informe o código do produto: '))
qtd = int(input('Informe a quantidade desejada: '))

if codigo == 1:
  resp = 4.0 * qtd
elif codigo == 2:
  resp = 4.5 * qtd
elif codigo == 3:
  resp = 5.0 * qtd
elif codigo == 4:
  resp = 2.0 * qtd
elif (codigo == 5):
  resp = 1.5 * qtd
  
print('Total: R$', '{:.2f}'.format(resp))