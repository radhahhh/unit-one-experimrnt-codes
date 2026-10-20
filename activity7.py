items = []

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

for i in range(n):
    name = input("Product name: ")
    price = float(input("Product price: "))
    quantity = int(input("Quantity: "))

    print("1. Food")
    print("2. Clothing")
    print("3. Electronics")

    category = int(input("Enter category: "))

    if price < 0 or quantity <= 0 or category not in (1, 2, 3):
        print("Invalid product details")
        continue

    amount = price * quantity

    if category == 1:
        tax_rate = 0.05
    elif category == 2:
        tax_rate = 0.12
    else:
        tax_rate = 0.18

    tax = amount * tax_rate
    item_total = amount + tax

    items.append((name, quantity, amount, tax, item_total))

    subtotal = subtotal + amount
    total_tax = total_tax + tax

if subtotal >= 5000:
    discount = subtotal * 0.10

    if discount > 1000:
        discount = 1000
else:
    discount = 0

grand_total = subtotal + total_tax - discount

print("\n--------- RETAIL INVOICE ---------")

for item in items:
    print("Product:", item[0])
    print("Quantity:", item[1])
    print("Amount:", round(item[2], 2))
    print("Tax:", round(item[3], 2))
    print("Item Total:", round(item[4], 2))
    print("--------------------")

print("Subtotal: Rs.", round(subtotal, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Discount: Rs.", round(discount, 2))
print("Grand Total: Rs.", round(grand_total, 2))
