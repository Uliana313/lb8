import numpy as np

A = np.random.randint(1, 24, size=12)
print("Одновимірний масив A:")
print(A)

B = A.reshape(3, 4)
print("\nДвомірний масив B:")
print(B)
