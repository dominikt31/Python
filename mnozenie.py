ile = 0
wywolania = ""


def A(m, n):
    global ile
    global wywolania
    if ile > 0:
        wywolania += f"A({int(m)}, {int(n)}) "
    ile += 1
    if n == 1:
        return m
    elif n%2 == 0:
        return A(2*m, n/2)
    elif n%2 == 1:
        return 2*A(m, (n-1)/2)+m
    
x = int(input("Podaj pierwsza liczbe: "))
y = int(input("Podaj druga liczbe: "))

print(f"Wynik: {A(x,y)}, {ile-1} iteracji")
print(wywolania)