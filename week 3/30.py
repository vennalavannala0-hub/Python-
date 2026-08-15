N = 4

# Upper half
for i in range(1, N + 1):
    print("* " * i + " " * (2 * (N - i)) + "* " * i)

# Lower half
for i in range(N - 1, 0, -1):
    print("* " * i + " " * (2 * (N - i)) + "* " * i)