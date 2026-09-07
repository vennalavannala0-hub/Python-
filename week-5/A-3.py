s = input()

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

for ch in count:
    if count[ch] > 1:
        print(ch, count[ch])