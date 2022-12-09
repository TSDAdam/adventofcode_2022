with open ('./09.in') as file:
    data = [line.strip() for line in file]

visited = [[0,0]]
directions = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}
knots = []
for x in range(10):
    knots.append([0,0])

for instruction in data:
    words = instruction.split()
    direction = words[0]
    amount = int(words[1])
    
    for _ in range(amount):
        knots[0][0] += directions[direction][0] # update the head x and y
        knots[0][1] += directions[direction][1]
        for i in range(1,10):
            gap = abs(knots[i-1][0] - knots[i][0]) + abs(knots[i-1][1] - knots[i][1])
            if gap == 2:
                if knots[i][0] == knots[i-1][0]: # on the same row as prev
                    if knots[i-1][1] > knots[i][1]:
                        knots[i][1] += 1
                    else:
                        knots[i][1] -= 1
                if knots[i][1] == knots[i-1][1]: # on the same col as prev
                    if knots[i-1][0] > knots[i][0]:
                        knots[i][0] += 1
                    else:
                        knots[i][0] -= 1
            if gap > 2:
                if knots[i-1][0] < knots[i][0] and knots[i-1][1] < knots[i][1]:
                    knots[i][0] -= 1
                    knots[i][1] -= 1
                    #print("tail moves downleft")
                if knots[i-1][0] < knots[i][0] and knots[i-1][1] > knots[i][1]:
                    knots[i][0] -= 1
                    knots[i][1] += 1
                    #print("tail moves upleft")
                if knots[i-1][0] > knots[i][0] and knots[i-1][1] > knots[i][1]:
                    knots[i][0] += 1
                    knots[i][1] += 1
                    #print("tail moves upright")
                if knots[i-1][0] > knots[i][0] and knots[i-1][1] < knots[i][1]:
                    knots[i][0] += 1
                    knots[i][1] -= 1
                    #print("tail moves downright")
        if i == 9 and knots[i] not in visited:
            visited.append(knots[i].copy())
print(visited)
        #print("head : {}, tail : {}".format(h,t))      
print(len(visited))