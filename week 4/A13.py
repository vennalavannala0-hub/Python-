numbers = [10, 25, 5, 40, 15]

maximum = numbers[0]
minimum = numbers[0]
total = 0

for number in numbers:
    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

    total += number

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)
