import random

T = []
znaleziono = False

for i in range(0, 10):
    T.append(random.randint(1,100))

liczba = int(input("Podaj liczbę do wyszukania "))
T.append(liczba)

for i in range(0, len(T)-1):
    if T[i] == liczba and i != len(T)-1:
        znaleziono = True
        print(f"Znaleziono {liczba} na indeksie {i}")
        break

if not znaleziono:
    print("Nie znaleziono liczby w tablicy")

print(T, liczba)
