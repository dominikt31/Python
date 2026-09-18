import random

class losowanie:
    def __init__(self):
        self.wylosowane = []
        self.ile = 0
        self.max = 0
        self.min = 0
        self.posortowana = True

    def wylosuj(self):
        self.ile = int(input("Podaj ile zmiennych chcesz wylosować: "))
        
        self.wylosowane = []

        for _ in range(self.ile):
            liczba = random.randint(1, 100)
            self.wylosowane.append(liczba)

        print("Wylosowane liczby:")
        print(self.wylosowane)

    def srednia(self):
        suma = sum(self.wylosowane)
        srednia = suma / self.ile
        print("Średnia wylosowanych liczb:", srednia)

    def max_min(self):
        self.min = self.wylosowane[0]
        self.max = self.wylosowane[0]

        for i in self.wylosowane:
            if i < self.min:
                self.min = i
            elif i > self.max:
                self.max = i

        print("Min:", self.min, ", Max:", self.max)

    def czyposortowana(self):
        for i in range(len(self.wylosowane) - 1):
            if self.wylosowane[i] > self.wylosowane[i + 1]:
                self.posortowana = False
        if self.posortowana:
            print("Lista jest posortowana")
        else:
            print("Lista nie jest posortowana")



def main():
    w = losowanie()
    w.wylosuj()
    w.srednia()
    w.max_min()
    w.czyposortowana() 

if __name__ == "__main__":
    main()
