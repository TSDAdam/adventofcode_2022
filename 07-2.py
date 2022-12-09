
with open ('./07.in') as file:
    data = [line.strip() for line in file]

filesizes = dict({"root": 0})

for row in data:
    if row == "$ cd /":
        currentDir = ["root"]   # start at the first entry, add it to a list of the paths, and call that first one 'root'
    elif row[0:7] == "$ cd ..":
        currentDir.pop()        # if it's cd .. , take the last path off the stack off paths
    elif row[0:4] == "$ cd":
        currentDir.append("/".join([currentDir[-1], row[5:]]))  # if we move up to a new dir, add it to the stack, joined with a '/'
        filesizes[currentDir[-1]] = 0                           # ...and start its filesize total at 0
    elif row[0].isdigit():                                      # if the first char is a digit, it must be a file size
        for file in currentDir:                                 # the tricky bit! if it's a file, 
            filesizes[file] += int(row.split(" ")[0])           # add it's value to every path in the tree as it stands.
            #print (content)
p1 = 0
for x in filesizes.values():                # part 1 - iterate through all the values
    if x <= 100000:                         # if that path is at most 100k
        p1 += x                             # add it to the total

p2 = []
for y in filesizes.values():                # part 2 - get all the values again
    if y >= filesizes['root'] - 40000000:   # we know the disk is 70M - so take the full occupied space at root,
        p2.append(y)                        # subtract 40M, and if your path is bigger, then it must free up the space
                                            # and make a list of those values  
print(p1)

print(min(p2))                              # part two wants the smallest matching dir to delete, so use min()