import random

class Lotto:
    def __init__(self):
        self.strzal = []
        self.wylosowane = []
        self.ile_liczb = 6
        self.licznik = 0

    def posortuj(self, tablica):
        dlugosc = len(tablica)
        for i in range (0, dlugosc-1):
            for j in range (0, dlugosc-i-1):
                if tablica[j] > tablica[j+1]:
                    temp = tablica[j]
                    tablica[j] = tablica[j+1]
                    tablica[j+1] = temp

    def wylosuj(self):
        tablica = []
        for _ in range(0, self.ile_liczb):
            tablica.append(random.randint(1,49))
        self.posortuj(tablica)
        for i in range (0, self.ile_liczb-1):
            if tablica[i] == tablica[i+1]:
                tablica = self.wylosuj()
        return tablica

    def czy_wygrana(self):
        wygrano = True
        for i in range(0, self.ile_liczb):
            if(self.strzal[i] != self.wylosowane[i]):
                wygrano = False
        if wygrano:
            print(f'Wygrano po {self.licznik} próbach\nWylosowane liczby:{self.strzal}')
            return True
        else:
            self.licznik += 1

    def zagraj_automatycznie(self):
        wygrano = False
        while not wygrano:
            self.strzal = self.wylosuj()
            self.wylosowane = self.wylosuj()
            wygrano = self.czy_wygrana()

def main():
    los = Lotto()
    los.ile_liczb = 5
    los.zagraj_automatycznie()

if __name__ == "__main__":
    main()