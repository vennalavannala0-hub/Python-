def is_even(n):
    """Return True if n is even, otherwise return False."""
    return n % 2 == 0


for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))

    if is_even(number):
        print(number, "is even.")
    else:
        print(number, "is odd.")