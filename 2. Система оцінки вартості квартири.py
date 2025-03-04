apartments = [
    {'time': 10, 'size': 120, 'quality': 10},
    {'time': 20, 'size': 70, 'quality': 5},
    {'time': 70, 'size': 50, 'quality': 1},
]

for i, apt in enumerate(apartments):
    price = (apt['size'] * apt['quality'] * 1000) / (apt['time'] + 1)
    print(f"Квартира {i+1}: {price:.2f} у.е.")
