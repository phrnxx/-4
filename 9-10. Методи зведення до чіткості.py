import skfuzzy as fuzz
import numpy as np

x = np.arange(0, 11, 1)
y = fuzz.trimf(x, [0, 5, 10]) 

центроїд = fuzz.defuzz(x, y, 'centroid')
print(f"Чітке значення (центроїд): {центроїд:.2f}")
