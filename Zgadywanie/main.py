min = 1
max = 500
correct = 333
guess = int(input(f"Podaj liczbe do zgadniecia ({min}-{max}) "))

while guess != correct:
    if guess < correct:
        min = (min+max) // 2
        print(f"{guess} to za malo, nowy przedzial: {min}-{max}, polowa: {(min+max) // 2}")
    else:
        max = (min+max) // 2
        print(f"{guess} to za duzo, nowy przedzial: {min}-{max}, polowa: {(min+max) // 2}")
        
    guess = int(input(f"Podaj liczbe do zgadniecia ({min}-{max}) "))
    
print("Liczba zgadnieta")