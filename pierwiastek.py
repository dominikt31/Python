import os

x = float(input('Podaj liczbe ktorej chcesz obliczyc pierwiastek: '))
epsilon = float(input('Podaj dokladnosc pierwiastka (np. 0.001): '))

b = x
a = 0

while abs(b-a) > epsilon:
    b = (a+b)/2
    a = x/b

print(f"Pierwiastek liczby {x} z dokładnością +-{epsilon} to {a}")

os.system("pause")