import random

T = []

for i in range(0, 10):
    T.append(random.randint(1,100))

for i in range(0, len(T)-1):
    for j in range(0, len(T)-i-1):
        if T[j] > T[j+1]:
            temp = T[j]
            T[j] = T[j+1]
            T[j+1] = temp

print(T)
