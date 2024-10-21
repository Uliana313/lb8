import array
import random

N = int(input("Введіть число N: "))
M = int(input("Введіть число M: "))

a = array.array('i', [random.randint(0, 100) for _ in range(N)])

for i in range(M):
    num = int(input(f"Введіть число {i+1}: "))
    a.append(num)

a = sorted(a, reverse=True)

print("Відсортований масив за спаданням:")
print(a) 
