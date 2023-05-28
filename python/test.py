strs = ["flower","flow","flight"]

shortest = min(strs, key=len)

print(shortest)

for i, char in enumerate(iterable=shortest):
    print(i, char)