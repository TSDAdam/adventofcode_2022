with open ('./09.in') as file:
    data = [line.strip() for line in file]

visited = [[0,0]]
directions = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}
h, t = [0,0], [0,0]

for instruction in data:
    words = instruction.split()
    direction = words[0]
    amount = int(words[1])
    
    for _ in range(amount):
        h[0] += directions[direction][0] # update the head x and y
        h[1] += directions[direction][1]
        if (h[0] == t[0]) and abs(h[1] - t[1]) > 1:     # row but a big gap in the column
            t[1] += directions[direction][1]            # move the tail too
            print("tail moves {}".format(direction))
        elif (h[1] == t[1]) and abs(h[0] - t[0]) > 1:   # same as above but for row
            t[0] += directions[direction][0]            # ...
            print("tail moves {}".format(direction))
        else:
            gap = abs(h[0] - t[0]) + abs(h[1] - t[1])
            if gap > 2:
                if h[0] < t[0] and h[1] < t[1]:
                    t[0] -= 1
                    t[1] -= 1
                    print("tail moves downleft")
                elif h[0] < t[0] and h[1] > t[1]:
                    t[0] -= 1
                    t[1] += 1
                    print("tail moves upleft")
                elif h[0] > t[0] and h[1] > t[1]:
                    t[0] += 1
                    t[1] += 1
                    print("tail moves upright")
                elif h[0] > t[0] and h[1] < t[1]:
                    t[0] += 1
                    t[1] -= 1
                    print("tail moves downright")
        if t not in visited:
            visited.append(t.copy())
print(visited)
        #print("head : {}, tail : {}".format(h,t))      
print(len(visited))