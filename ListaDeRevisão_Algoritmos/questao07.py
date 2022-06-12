s = int(input('Informe a hora de partida: '))
t = int(input('Informe o tempo de viagem: '))
f = int(input('Informe a diferença de fuso horário: '))

hd = s + t + f
hd = int(hd)

if 0 <= hd < 24:
    print(hd)
elif hd >= 24:
    print(hd - 24)
elif hd < 0:
    print(24 + hd)