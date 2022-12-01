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
max = 0

print(elves)
for elf in elves: # part 1
    if elf > max:
        max = elf
print(max)

# part 2
totals = []
for elf in elves:
    totals.append(elf)
totalset = set(totals)
totalset = sorted(totalset, reverse=True)

print(sum(totalset[:3]))