dia1 = int(input('Temperatura do 1° dia: '))
dia2 = int(input('Temperatura do 2° dia: '))
dia3 = int(input('Temperatura do 3° dia: '))

if dia1 > dia2 <= dia3:
  print(':)')

elif dia1 < dia2 >= dia3:
  print(':(')

elif dia1 < dia2 < dia3 and (dia3 - dia2) < (dia2 - dia1):
  print(':(')  

elif dia1 < dia2 < dia3 and (dia3 - dia2) >= (dia2 - dia1):
  print(':)')

elif dia1 > dia2 > dia3 and (dia3 - dia2) < (dia2 - dia1):
  print(':)')

elif dia1 > dia2 > dia3 and (dia3 - dia2) <= (dia2 - dia1):
  print(':(')  

elif dia1 == dia2 < dia3:
  print(':)')

elif dia1 == dia2 > dia3:
  print(':(')