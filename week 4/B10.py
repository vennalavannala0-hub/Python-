numbers = (10, 20, 30, 40, 50)

try:
    # Attempt to modify an element
    numbers[2] = 100
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable and cannot be modified.")
