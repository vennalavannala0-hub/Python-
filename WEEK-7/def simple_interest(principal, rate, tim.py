def simple_interest(principal, rate, time):
    """Calculate and return simple interest using the formula SI = (P * R * T) / 100."""
    return (principal * rate * time) / 100


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time (in years): "))

interest = simple_interest(principal, rate, time)

print("Simple Interest:", interest)