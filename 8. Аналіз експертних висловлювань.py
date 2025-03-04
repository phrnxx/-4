price = {'cheap': 50000, 'moderate': 100000, 'expensive': 200000}
size = {'small': 40, 'medium': 80, 'large': 120}

expert_input = {'price': 'expensive', 'size': 'small'}
final_price = price[expert_input['price']] / size[expert_input['size']]
print(f"Ціна за 1 м²: {final_price:.2f} у.е.")
