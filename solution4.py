from collections import deque, defaultdict
from copy import deepcopy


def answer(map_in):
    walls = deepcopy(map_in)
    res = dfs(map_in, walls, False)
    while True:
        tmp = dfs(map_in, walls, True)
        if tmp is None:
            return res
        if tmp < res:
            res = tmp


def dfs(map_in, walls, knock):
    s = set()
    q = deque()
    par = defaultdict()
    par['0,0'] = None
    s.add('0,0')
    q.append('0,0')
    knocked_down = False
    while len(q) != 0:
        curr = q.popleft()
        if curr == ''.join([str(len(map_in[0])-1), ',', str(len(map_in)-1)]):
            break
        x = int(curr.split(',')[0])
        y = int(curr.split(',')[1])
        if (y < len(map_in) - 1 and map_in[y+1][x] == 0) or (knock and not knocked_down and y < len(map_in) - 2 and map_in[y+1][x] == 1 and map_in[y+2][x] == 0 and walls[y+1][x] == 1):
            if ''.join([str(x), ',', str(y+1)]) not in s:
                s.add(''.join([str(x), ',', str(y+1)]))
                par[''.join([str(x), ',', str(y+1)])] = curr
                q.append(''.join([str(x), ',', str(y+1)]))
                if map_in[y+1][x] == 1:
                    walls[y+1][x] = 0
                    knocked_down = True
        if (y > 0 and map_in[y-1][x] == 0) or (knock and not knocked_down and y > 1 and map_in[y-1][x] == 1 and map_in[y-2][x] == 0 and walls[y-1][x] == 1):
            if ''.join([str(x), ',', str(y-1)]) not in s:
                s.add(''.join([str(x), ',', str(y-1)]))
                par[''.join([str(x), ',', str(y-1)])] = curr
                q.append(''.join([str(x), ',', str(y-1)]))
                if map_in[y-1][x] == 1:
                    walls[y-1][x] = 0
                    knocked_down = True
        if (x < len(map_in[0]) - 1 and map_in[y][x+1] == 0) or (knock and not knocked_down and x < len(map_in[0]) - 2 and map_in[y][x+1] == 1 and map_in[y][x+2] == 0 and walls[y][x+1] == 1):
            if ''.join([str(x+1), ',', str(y)]) not in s:
                s.add(''.join([str(x+1), ',', str(y)]))
                par[''.join([str(x+1), ',', str(y)])] = curr
                q.append(''.join([str(x+1), ',', str(y)]))
                if map_in[y][x+1] == 1:
                    walls[y][x+1] = 0
                    knocked_down = True
        if (x > 0 and map_in[y][x-1] == 0) or (knock and not knocked_down and x > 1 and map_in[y][x-1] == 1 and map_in[y][x-2] == 0 and walls[y][x-1] == 1):
            if ''.join([str(x-1), ',', str(y)]) not in s:
                s.add(''.join([str(x-1), ',', str(y)]))
                par[''.join([str(x-1), ',', str(y)])] = curr
                q.append(''.join([str(x-1), ',', str(y)]))
                if map_in[y][x-1] == 1:
                    walls[y][x-1] = 0
                    knocked_down = True
    res = 0
    curr = ''.join([str(len(map_in[0])-1), ',', str(len(map_in)-1)])
    if knock and not knocked_down:
        return None
    while True:
        res += 1
        if curr == '0,0':
            return res
        try:
            curr = par[curr]
        except:
            return float('inf')


print(str(answer([[0]])))
print(str(answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])))
print(str(answer([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])))
print(str(answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])))
print(str(answer([[0]*5]*8)))
print(str(answer([[0]*1]*8)))
print(str(answer([[0]*5]*1)))
print(str(answer([[0]*100]*100)))
