with open ('./08.in') as file:
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
        for checkLeft in range(x -1, -1, -1): # check the trees left of the current tree
            treesLeft += 1
            if trees[y][checkLeft]["height"] >= trees[y][x]["height"]:
                break
        for checkRight in range(x + 1, MAXX): # check the trees right of the current tree
            treesRight += 1
            if trees[y][checkRight]["height"] >= trees[y][x]["height"]:
                break

        for checkUp in range(y -1, -1, -1): # check the trees up of the current tree
            treesUp += 1
            if trees[checkUp][x]["height"] >= trees[y][x]["height"]:
                break

        for checkDown in range(y + 1, MAXY): # check the trees down of the current tree
            treesDown += 1
            if trees[checkDown][x]["height"] >= trees[y][x]["height"]:
                break

        trees[y][x]["treesVisible"] = (treesLeft * treesRight * treesUp * treesDown)
        treesLeft, treesRight, treesUp, treesDown = 0, 0, 0, 0


maxTree = 0
for row in trees:
    for tree in row:
        if tree["treesVisible"] >= maxTree:
            maxTree = tree["treesVisible"]

#for row in trees:
 #   print(row)

print(maxTree)        