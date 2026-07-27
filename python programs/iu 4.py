numbers = input("Enter numbers separated by spaces: ")

# Split the input and convert each value to integer
nums = list(map(int, numbers.split()))

# Calculate and print the sum
print("Sum:", sum(nums))