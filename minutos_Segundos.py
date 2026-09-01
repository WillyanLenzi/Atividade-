minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

tempo = minutos * 60 + segundos

for i in range(tempo, -1, -1):
    minutos = i // 60
    segundos = i % 60

    print(f"{minutos:02d}:{segundos:02d}")
