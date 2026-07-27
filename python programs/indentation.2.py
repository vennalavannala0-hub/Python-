for i in range(1, 3):          # Outer for loop
    print("Loop", i)

    for num in range(1, 11):   # Inner for loop
        if num % 2 == 0:       # Check even
            print(num, "Even")
        else:                  # Check odd
            print(num, "Odd")