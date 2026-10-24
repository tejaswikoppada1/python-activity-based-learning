
# Multi-Product Shopping Budget Constraint

products = {
    "Laptop": [50000, 1],
    "Headphones": [3000, 2],
    "Mouse": [1000, 2],
    "Keyboard": [2000, 1]
}

budget = 55000

# Calculate total cost
total = 0

for product, details in products.items():
    price = details[0]
    quantity = details[1]
    total += price * quantity

print("Total before discount:", total)

# Apply 10% discount if total is above Rs. 50,000
if total > 50000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("Discount:", discount)
print("Final amount:", final_amount)
print("Budget:", budget)

# Check budget
if final_amount <= budget:
    print("Shopping is within the budget.")
    print("Remaining amount:", budget - final_amount)

else:
    extra = final_amount - budget
    print("Shopping exceeds the budget by:", extra)
    print("\nPurchases that can be reduced:")

    # Reduce quantities of non-essential items first
    for product in ["Keyboard", "Mouse", "Headphones"]:
        price = products[product][0]
        quantity = products[product][1]

        while quantity > 0 and final_amount > budget:
            quantity -= 1
            final_amount -= price
            products[product][1] = quantity

        if final_amount <= budget:
            break

    print("\nUpdated shopping basket:")
    for product, details in products.items():
        print(product, ":", details[1])

    print("Final cost:", final_amount)
    print("Remaining budget:", budget - final_amount)

