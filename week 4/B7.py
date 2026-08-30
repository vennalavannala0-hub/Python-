numbers = (10, 25, 5, 40, 25, 15, 25)

# Find maximum and minimum without using max() or min()
maximum = numbers[0]
minimum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number

# Count occurrences of a given value
value = 25
count = numbers.count(value)

print("Tuple:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Count of", value, ":", count)
