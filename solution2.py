import math

def answer(source, dest):
    d_x = abs(source % 8 - dest % 8)
    d_y = abs(source / 8 - dest / 8)
    if d_x < d_y:
        d_x, d_y = d_y, d_x
    if d_x == 1 and d_y == 0:
        return 3
    if d_x == 2 and d_y == 2:
        return 4
    d = d_x - d_y
    if d_y > d:
        return int(d - 2*math.floor((d-d_y)/3))
    else:
        return int(d - 2*math.floor((d-d_y)/4))


print(str(answer(0, 17)))
print(str(answer(0, 27)))

