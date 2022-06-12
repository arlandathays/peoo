numbers = [10, 20]
items = ["Mesa", "Cadeira"]

for x in numbers:
  for y in items:
    print(x, y)

#Resposta:
#O loop imprime o 1° valor da lista "numbers" com o 1° valor da lista "items"
#Depois, imprime novamente o 1° valor da lista "numbers", mas dessa vez seguido pelo 2° valor da lista "items"
#Repete o processo, agora começando pelo 2° valor da lista "numbers" acompanhado pelo 1° valor da lista "items"
#E em seguida, o 2° valor da lista "numbers" acompanhado pelo 2° valor da lista "items"

#Um valor de uma das listas é impresso junto com um valor da outra lista
#Esse processo se repete até que o primeiro valor da primeira lista tenha sido impresso com todos os valores da outra lista
#Após isso, o 2° valor da lista será impresso com todos os valores da outra lista e assim por diante
#O ponto de referência é a lista no "for" maior
#Se inverter a posição das listas nos laços, a lista "items" passará a ser o referencial e portanto terá seus valores impressos primeiro