from copy import deepcopy

with open ('./14.in') as file:
    data = file.read().strip()

cave = {}
xs, ys = [], []
lines = []
maxy, maxx, miny, minx = 0, 0, 999, 999

for line in data.split('\n'):
    prevcoords = (-1, -1)
    for coord in line.split(' -> '):
        x, y = coord.split(',')
        x, y = int(x), int(y)
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)
        if prevcoords[0] > -1:
            fromy = min(y, prevcoords[1])
            toy = max(y, prevcoords[1])
            fromx = min(x, prevcoords[0])
            tox = max(x, prevcoords[0])
            for yy in range(fromy, toy + 1):
                for xx in range(fromx, tox + 1):
                    cave[(xx,yy)] = '#'
        prevcoords = (x, y)
print(cave)

cave2 = deepcopy(cave)

for y in range(miny, maxy):
    string = ""
    for x in range(minx, maxx):
        if (x,y) in cave.keys():
            string += cave[(x,y)]
        else:
            string += "."
    print(string)

def canmovedown(x, y):
    if (x, y+1) not in cave:
        return True
    return False

def canmoveleft(x, y):
    if (x-1, y+1) not in cave:
        return True
    return False

def canmoveright(x, y):
    if (x+1, y+1) not in cave:
        return True
    return False

sand = 0
stopnow = False
while not stopnow:
    sand += 1
    blocked = False
    x = 500
    y = 0
    while not blocked:
        if y > maxy:
            stopnow = True
            break
        if canmovedown(x, y):
            y += 1
        elif canmoveleft(x, y):
            x -= 1
            y += 1
        elif canmoveright(x, y):
            x += 1
            y += 1
        else:
            cave[(x,y)] = 'o'
            blocked = True

        if y > maxy:
            stopnow = True
print(sand -1)


# Part two

def canmovedown2(x, y):
    if (x, y+1) not in cave2:
        return True
    return False

def canmoveleft2(x, y):
    if (x-1, y+1) not in cave2:
        return True
    return False

def canmoveright2(x, y):
    if (x+1, y+1) not in cave2:
        return True
    return False


for x in range(minx - maxy, maxx + maxy):
    cave2[(x,maxy + 2)] = '#'

sand = 0
stopnow = False
while not stopnow:
    sand += 1
    blocked = False
    x = 500
    y = 0
    while not blocked:
        if canmovedown2(x, y):
            y += 1
        elif canmoveleft2(x, y):
            x -= 1
            y += 1
        elif canmoveright2(x, y):
            x += 1
            y += 1
        else:
            cave2[(x,y)] = 'o'
            blocked = True
            print("blocked at {}, {}".format(x,y))
            if x == 500 and y == 0:
                stopnow = True


print(x, y, sand -1)