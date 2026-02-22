# homework8_george_okuro.py
# Week 7: Python User Input and While Loops

# List of pizza orders
pizza_orders = [
    "Pepperoni",
    "Cheese",
    "Veggie",
    "BBQ Chicken",
    "Hawaiian"
]

# Empty list for finished pizzas
finished_pizzas = []

# Process each pizza order
while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print("Your pizza pie is finished!")
    finished_pizzas.append(current_pizza)

print("\nAll pizzas have been made:\n")

# Print finished pizzas
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")