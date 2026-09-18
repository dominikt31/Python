import random

class Lotto:
    def __init__(self):
        self.strzal = []
        self.wylosowane = []
        self.licznik = 0

    def posortuj(self, tablica):
        dlugosc = len(tablica)
        for i in range (0, dlugosc-1):
            for j in range (0, dlugosc-i-1):
                if tablica[j] > tablica[j+1]:
                    temp = tablica[j]
                    tablica[j] = tablica[j+1]
                    tablica[j+1] = temp

    def wylosuj(self, tablica):
        for _ in range(0,6):
            tablica.append(random.randint(1,49))
        self.posortuj(tablica)
        for i in range (0,5):
            if tablica[i] == tablica[i+1]:
                tablica = []
                self.wylosuj(tablica)
            print(tablica)

    def zagraj_automatycznie(self):
        self.wylosuj(self.strzal)

def main():
    los = Lotto()
    los.zagraj_automatycznie()

if __name__ == "__main__":
    main()