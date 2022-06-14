num=int(input("Digite um número maior que 0: "))
num0=int(0)
num1=int(1)
fib=int(0)
if num==1:
  num0=0
else:
  for c in range(1,num):
    fib=num0+num1
    num0=num1
    num1=fib
    print(num0)
print("Fib",num,"=",fib)