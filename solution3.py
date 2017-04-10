import math


def answer(h, q):
    res = []
    for i in q:
        par = int(math.pow(2, h) - 1)
        if i >= par:
            res.append(-1)
            continue
        mid = par/2
        level = h
        while True:
            if i == par - 1 or i == int(mid):
                res.append(par)
                break
            if i > mid:
                par -= 1
                mid += math.pow(2, level - 2) - 1
            else:
                par = int(mid)
                mid -= math.pow(2, level - 2)
            level -= 1
    return res


# print(str(answer(4, [1])))
# print(str(answer(4, [8])))
# print(str(answer(4, [12])))
# print(str(answer(4, [1])))
print(str(answer(3, [7, 3, 5, 1])))
print(str(answer(5, [19, 14, 28])))
print(str(answer(3, range(1, 8))))
print(str(answer(4, range(1, 16))))
# print(str(answer(5, range(1, 32))))
# print(str(answer(30, range(1, 10000))))
