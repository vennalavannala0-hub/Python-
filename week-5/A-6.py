def my_find(s, sub):
    n = len(s)
    m = len(sub)

    for i in range(n - m + 1):
        if s[i:i + m] == sub:
            return i

    return -1


s = input()
sub = input()

print(my_find(s, sub))