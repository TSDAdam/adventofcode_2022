import string
from collections import defaultdict, deque


with open ('./12x.in') as file:
    data = [line.strip() for line in file]

heights = string.ascii_lowercase
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 'S':
            start = (y,x)
        elif data[y][x] == 'E':
            end = (y,x)

neighbours = defaultdict(list)
predecessors = []
peakheights = {}

def get_neighbours(y,x):
    for yy in range(y-1, y+2):
        for xx in range(x-1, x+2):
            if (yy >= 0 and yy < len(data)) and (xx >= 0 and xx < len(data[0])):
                if (xx, yy) != (x, y):
                    if(abs(xx) != abs (yy)):  # my long-winded way of saying for x in 0,1 1,0 -1,0 0,-1 
                        height = heights.find(data[y][x])  
                        if (heights.find(data[yy][xx]) <= height + 1):
                            neighbours[(y,x)].append((yy,xx))
                            peakheights[(yy,xx)] = heights.find(data[yy][xx])



for y, row in enumerate(data):
    for x, space in enumerate(row):
        get_neighbours(y, x) 

print(neighbours)
print("heights")
print(peakheights)

Q = deque
Visited = []
Q.append(start)

while True:
    