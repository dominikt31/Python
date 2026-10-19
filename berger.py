T = []
IP = [0, "Anka", "Emilka", "Dominik", "Natan", "Kuba", "Rafal", "Kacper", "Filip"]

kolejka = 1
n=8

for i in range(0, n+1):
    T.append(i)
    
print(f"-----\nKolejka nr.{kolejka}\n-----")

for i in range(1, n//2 + 1):
    print(f"{IP[T[i]]} - {IP[T[n-i+1]]}")

kolejka += 1


for j in range(kolejka, n):

    print(f"-----\nKolejka nr.{kolejka}\n-----")

    for i in range(1, n):
        T[i] = (T[i] + n//2 - 2) % (n - 1) + 1
        
        
    for i in range(1, n//2 + 1):
        if kolejka % 2 == 0 and i == 1:
            print(f"{IP[T[n-1+1]]} - {IP[T[i]]}")
        else:
            print(f"{IP[T[i]]} - {IP[T[n-i+1]]}")
        
    kolejka += 1
