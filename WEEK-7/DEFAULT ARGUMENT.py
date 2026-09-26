def calculate_price(price, tax_rate=18, discount=0):
    """Calculate the final price after applying tax and discount."""
    tax = price * tax_rate / 100
    final_price = price + tax - discount
    return final_price


# (a) Only price
result1 = calculate_price(1000)
print("Final price (default tax and discount):", result1)

# (b) Price and custom tax rate
result2 = calculate_price(1000, 10)
print("Final price (custom tax rate):", result2)

# (c) All three arguments overridden
result3 = calculate_price(1000, 12, 100)
print("Final price (custom tax and discount):", result3)