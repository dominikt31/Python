x = input('Podaj liczbe ktorej chcesz obliczyc pierwiastek: ')
epsilon = input('Podaj dokladnosc pierwiastka (np. 0.001): ')

x = float(x)
epsilon = float(epsilon)

b = x
a = 0

while abs(b-a) > epsilon:
    b = (a+b)/2
    a = x/b

print(f"Pierwiastek liczby {x} z dokładnością {epsilon} to {a}")