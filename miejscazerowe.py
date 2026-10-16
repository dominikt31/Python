def f(x):
    return x**3 - 3*x**2 - 4*x + 12

def miejscezerowe(x1, x2, epsilon):
    
    if(x1 > x2):
        temp = x1
        x1 = x2
        x2 = temp
        
    x1orig = x1
    x2orig = x2
    
    if f(x1) * f(x2) > 0:
        print("Brak miejsc zerowych/Wiecej niz jedno miejsce zerowe")
    else:
        pol = (x1 + x2) / 2
        while(abs(f(pol)) > epsilon):
            print(f(pol), pol, x1, x2)
            pol = (x1 + x2) / 2
            if(f(pol) > 0):
                x2 = pol
            else:
                x1 = pol
        print(f"Miejsce zerowe funkcji x^3 - 3x^2 - 4x + 12 w przedziale {x1orig}, {x2orig} wynosi {pol}")
            
x1 = float(input("Podaj x1 "))
x2 = float(input("Podaj x2 "))
epsilon = float(input('Podaj dokladnosc pierwiastka (np. 0.001): '))

miejscezerowe(x1, x2, epsilon)