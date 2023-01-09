import random

ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))


liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

print("Wylosowane liczby:", liczby)