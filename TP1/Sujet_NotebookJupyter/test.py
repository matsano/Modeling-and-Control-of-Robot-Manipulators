import numpy as np

# Array unidimensional
vetor = np.array([3, 4])

print(vetor)

# Calcular a norma do vetor
norma = np.linalg.norm(vetor, ord=1)

print("Norma do vetor:", norma)
