def order_summary(customer, *items, discount=0, **extra):
    """Print an order summary using positional, *args, keyword, and **kwargs."""
    
    print("===== Order Summary =====")
    print("Customer:", customer)

    print("\nOrdered Items:")
    for item in items:
        print("-", item)

    print("\nDiscount:", discount, "%")

    print("\nExtra Information:")
    for key, value in extra.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    print("=========================")


# Calling the function with all four argument types
order_summary(
    "Meera",
    "Laptop",
    "Mouse",
    discount=10,
    delivery_address="Hyderabad",
    gift_wrap=True
)