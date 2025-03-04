import skfuzzy as fuzz
import numpy as np

x = np.arange(0, 11, 1)
y = fuzz.trimf(x, [0, 5, 10])  

centroid = fuzz.defuzz(x, y, 'centroid')
print(f"Чітке значення (центроїд): {centroid:.2f}")
