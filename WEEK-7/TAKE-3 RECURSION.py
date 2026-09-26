def factorial(n):
    """Return the factorial of a non-negative integer using recursion."""
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)


def factorial_iterative(n):
    """Return the factorial of a non-negative integer using iteration."""
    if n < 0:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Recursive factorial:", factorial(n))
    print("Iterative factorial:", factorial_iterative(n))