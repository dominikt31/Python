x = int(input("Podaj liczbe czterocyfrowa: "))
ile = 0

while (x != 6174 and ile < 100):
    ile += 1
    L = []
    
    while (x != 0):
        L.append(x%10)
        x=x//10

    desc = 0
    asc = 0

    for i in sorted(L):
        asc *= 10
        asc += i

    for i in sorted(L, reverse=True):
        desc *= 10
        desc += i

    x = desc - asc
    print(f"{x} = {desc} - {asc}, proba nr.{ile}")
    