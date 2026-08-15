N = 5

for i in range(1, N + 1):
    letter = chr(64 + i)
    for j in range(i):
        print(letter, end=" ")
    print()