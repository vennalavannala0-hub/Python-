# (a) Swapping values using a temporary third variable

a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)


# (b) Swapping values using Python's tuple unpacking

x = 30
y = 40

print("Before swapping:")
print("x =", x)
print("y =", y)

x, y = y, x

print("After swapping:")
print("x =", x)
print("y =", y)