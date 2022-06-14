numero = int(input('Digite um número: '))
num=[]
for i in range(len(str(numero)),0,-1):
  num.append(i)
for i in range(len(num),0,-1):
  print(num)
  num.remove(i)