data = []

with open ('./01.in') as file:
    for line in file.readlines():
        data.append(line.strip())

elves = []
currentelf = []
for row in data:
    if len(row) > 0:
        currentelf.append(int(row))
    else:
        elves.append(sum(currentelf))
        currentelf = []
elves.append(sum(currentelf)) 

elves.sort(reverse=True)

print(elves[0]) # part 1

print(sum(elves[:3])) # part 2