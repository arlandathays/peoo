num = []
for i in range(10):
  num.append(float(input('\nDigite um número real: ')))
print(f'\n {num}')

media = sum(num)/len(num)
print(f'\nA média dos elementos da lista é: {media}')

def buscarMaior(num):
  maior = num[0]
  for i in num:
    if i > maior:
      maior = i
  return maior

def buscarMenor(num):
  menor = num[0]
  for i in num:
    if i < menor:
      menor = i
  return menor

positivo = 0
negativo = 0
for i in num:
  if i >= 0:
    positivo += 1
  else:
    negativo +=1

print(f'\nO maior elemento da lista é: {buscarMaior(num)}')
print(f'\nO menor elemento da lista é: {buscarMenor(num)}')
print(f'\nA lista possui {positivo} números positivos.')
print(f'\nA lista possui {negativo} números negativos.')