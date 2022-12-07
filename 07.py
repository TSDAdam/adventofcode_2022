from collections import defaultdict

with open ('./07.in') as file:
    data = [line.strip() for line in file]

contains = defaultdict(list)
containedIn = defaultdict(list)
dirsizes = defaultdict(int)

def ls(pwd, contents):
    for row in contents:
        entry, arg = row.split(" ")
        if entry == "dir":              # if this row is a dir
            contains[pwd].append(arg)   # add it to the list of dirs the current dir contains
            containedIn[arg].append(pwd)
        else:
            dirsizes[pwd] += int(entry)
            # print(contains, dirsizes)

i = 0
while i < len(data) -1:
    firstspace = data[i].find(" ")
    text, values = data[i][:firstspace], data[i][firstspace+1:]
    if text == "$":         # ENTRY BY THE USER
        command = values[:2]
        if command == "cd":     
            directory = values[3:]
            if directory != "..":
                pwd = directory    # Change to the called dir if not ..
            else: 
                pwd = containedIn[directory]  # Else check the contained in dir to see where it lives, and jump back up
            i += 1
        elif command == "ls":
            i += 1
            contents = []
            while data[i][0] != "$" and i < len(data) -1:
                contents.append(data[i])
                i += 1
            ls(pwd, contents)
            
print(dirsizes)
print(contains)

deepdirsize = defaultdict(int)

def getsubdirsize(currentdir):
    deepdirsize[currentdir] = dirsizes[currentdir]
    if currentdir in contains:
        for subdir in contains[currentdir]:
            deepdirsize[currentdir] += getsubdirsize(subdir)
    return dirsizes[currentdir]

t=0
for subdir in contains['/']:
    getsubdirsize(subdir)

print(deepdirsize)

p1 = 0
for dir, size in deepdirsize.items():
    if size <= 100000:
        p1 += size
print(p1)