# (a) Square of a number
square = lambda x: x * x

# (b) Check if a number is even
is_even = lambda x: x % 2 == 0

# (c) Find the larger of two numbers
larger = lambda x, y: x if x > y else y


# Sample inputs
print("Square of 5:", square(5))
print("Is 8 even?:", is_even(8))
print("Is 7 even?:", is_even(7))


print("Larger of 10 and 25:", larger(10, 25))
grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks_list = [85, 35, 67, 28, 45, 90]

for marks in marks_list:
    print(marks, ":", grade(marks))

    # List of students and their marks
students = [
    ("Ravi", 78),
    ("Sita", 92),
    ("Amit", 65)
]

# Sort students by marks in descending order
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)

print("Students sorted by marks:")
for student in sorted_students:
    print(student)


# List of strings
names = ["Ravi", "Sita", "Amit", "Priya", "Raj"]

# Sort strings by length
sorted_names = sorted(names, key=lambda name: len(name))

print("\nNames sorted by length:")
for name in sorted_names:
    print(name)


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use map() to find cubes
cubes = list(map(lambda x: x ** 3, numbers))

# Use filter() to find numbers divisible by 3
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

print("Original numbers:", numbers)
print("Cubes:", cubes)
print("Numbers divisible by 3:", divisible_by_3)


items = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}

# Sort items by price from cheapest to most expensive
sorted_items = sorted(items.items(), key=lambda item: item[1])

print("Items sorted by price:")

for item, price in sorted_items:
    print(item, ":", price)