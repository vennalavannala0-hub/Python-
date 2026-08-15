N = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

while count < N:
    print(a, end=" ")
    a, b = b, a + b
    count += 1