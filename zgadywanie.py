import random

min = 1
max = 1000
correct = random.randint(min, max)
guess = int(input(f"Podaj liczbe do zgadniecia ({min}-{max}), polowa: {(min+max) // 2} | "))

while guess != correct:
    if guess < correct:
        min = guess
        print(f"{guess} to za malo")
    else:
        max = guess
        print(f"{guess} to za duzo")
        
    guess = int(input(f"Podaj liczbe do zgadniecia ({min}-{max}), polowa: {(min+max) // 2} | "))
    
print("Liczba zgadnieta")