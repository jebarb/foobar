from collections import defaultdict

def answer(data, n):
    count = defaultdict(int)
    for i in data:
        count[i] += 1
        if count[i] > n:
            data = [x for x in data if x != i]
    return data

print(str(answer([1, 2, 3], 0)))
print(str(answer([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)))
