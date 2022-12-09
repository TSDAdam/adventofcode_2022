with open ('./08.ina') as file:
    data = [line.strip() for line in file]
    grid = []
    for row in data:
        gridrow = []
        for val in row:
            gridrow.append(int(val))
        grid.append(gridrow)


MAXX = len(data[0])
MAXY = len(data)

trees = []

for y in range(0, MAXY):
    treerow = []
    for x in range(0, MAXX):
        treerow.append({
            "height": grid[y][x],
            "blockedUp": False,
            "blockedDown": False,
            "blockedLeft": False,
            "blockedRight": False,
            "visible": True,
            "treesVisible": 0
        })
    trees.append(treerow)

# PART ONE
for y in range(1, MAXY):
    for x in range(1, MAXX):
        for checkLeft in range(x): # check the trees left of the current tree
            if trees[y][checkLeft]["height"] >= trees[y][x]["height"]:
                trees[y][x]["blockedLeft"] = True

        for checkRight in range(x + 1, MAXX): # check the trees right of the current tree
            if trees[y][checkRight]["height"] >= trees[y][x]["height"]:
                trees[y][x]["blockedRight"] = True

        for checkUp in range(y): # check the trees up of the current tree
            if trees[checkUp][x]["height"] >= trees[y][x]["height"]:
                trees[y][x]["blockedUp"] = True

        for checkDown in range(y + 1, MAXY): # check the trees down of the current tree
            if trees[checkDown][x]["height"] >= trees[y][x]["height"]:
                trees[y][x]["blockedDown"] = True

for row in trees:
    for tree in row:
        if tree["blockedUp"] and tree["blockedDown"] and tree["blockedLeft"] and tree["blockedRight"]:
            tree["visible"] = False


p1 = 0
for row in trees:
    for tree in row:
        if tree["visible"]:
            p1 += 1

print(p1)

# PART TWO
for y in range(0, MAXY):
    for x in range(0, MAXX):
        treesLeft, treesRight, treesUp, treesDown = 0, 0, 0, 0

        breaknow = False
        biggestSeen = 0
        for checkLeft in range(x - 1, -1, -1): # check left
            if not breaknow:
                if trees[y][checkLeft]["height"] == trees[y][x]["height"]:  # if the tree to the left is the same height
                    treesLeft += 1
                    breaknow = True                                           # I can see one to the left
                    break                                                   # stop looking left
                if trees[y][checkLeft]["height"] < biggestSeen:
                    breaknow = True             # if the next tree is shorter than the biggest seen so far
                    break                                                   # we can't see it. don't count it. stop looking left
                if trees[y][checkLeft]["height"] > trees[y][x]["height"]:   # if the next tree is taller than my tree
                    treesLeft += 1
                    breaknow = True                                         # count it
                    break                                                   # and stop there
                treesLeft += 1                                              # if it hasn't stopped yet, add one to the count
                if trees[y][checkLeft]["height"] > biggestSeen:             # if this next tree is the biggest we've seen                      
                    biggestSeen = trees[y][checkLeft]["height"]             # mark its height as the biggest seen so far
            
        biggestSeen = 0
        breaknow = False
        for checkRight in range(x + 1, MAXX): # check the trees right of the current tree
            if not breaknow:
                if trees[y][checkRight]["height"] == trees[y][x]["height"]:
                    treesRight += 1
                    breaknow = True
                    break
                if trees[y][checkRight]["height"] < biggestSeen:
                    breaknow = True
                    break
                if trees[y][checkRight]["height"] > trees[y][x]["height"]:
                    treesRight += 1
                    breaknow = True
                    break
                treesRight += 1
                if trees[y][checkRight]["height"] > biggestSeen:
                    biggestSeen = trees[y][checkRight]["height"]

        biggestSeen = 0
        breaknow = False
        for checkUp in range(y - 1, -1, -1): # check the trees up of the current tree
            if not breaknow:
                if trees[checkUp][x]["height"] == trees[y][x]["height"]:
                    treesUp += 1
                    breaknow = True
                    break
                if trees[checkUp][x]["height"] < biggestSeen:
                    breaknow = True
                    break 
                if trees[checkUp][x]["height"] > trees[y][x]["height"]:
                    treesUp += 1
                    breaknow = True
                    break
                treesUp += 1
                if trees[checkUp][x]["height"] > biggestSeen:
                    biggestSeen = trees[checkUp][x]["height"]
           
        biggestSeen = 0
        breaknow = False
        for checkDown in range(y + 1, MAXY):
            if not breaknow: # check the trees down of the current tree
                if trees[checkDown][x]["height"] == trees[y][x]["height"]:
                    treesDown = 1
                    breaknow = True
                    break
                if trees[checkDown][x]["height"] < biggestSeen:
                    breaknow = True
                    break
                if trees[checkDown][x]["height"] > trees[y][x]["height"]:
                    treesDown += 1
                    breaknow = True
                    break
                treesDown += 1
                if trees[checkDown][x]["height"] > biggestSeen:
                    biggestSeen = trees[checkDown][x]["height"]

        #print("tree {} {} can see {} trees left, {} trees right, {} trees up, {} trees down".format(y, x, treesLeft, treesRight, treesUp, treesDown))
        trees[y][x]["treesVisible"] = treesLeft * treesRight * treesUp * treesDown
        treesLeft, treesRight, treesUp, treesDown = 0, 0, 0, 0

maxTree = 0
for row in trees:
    for tree in row:
        if tree["treesVisible"] >= maxTree:
            maxTree = tree["treesVisible"]

#for row in trees:
 #   print(row)

print(maxTree)        