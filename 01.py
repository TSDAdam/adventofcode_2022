data = []

with open ('./01.in') as file:              # my standard file read 
    for line in file.readlines():
        data.append(line.strip())

elves = []                                  # an empty list for the elves (totals of calories)
currentelf = []                             # an empty list to add each value to for the current elf
for row in data:
    if len(row) > 0:                        # if there's a number on this row,
        currentelf.append(int(row))         # add it to the current elf
    else:
        elves.append(sum(currentelf))       # otherwise add the elf to the list,
        currentelf = []                     # and make a new, blank elf to start again with
elves.append(sum(currentelf))               # the last elf on the list never gets finished by a blank row, so add them on after the loop

elves.sort(reverse=True)                    # sort the elves descending in value

print(elves[0])                             # part 1

print(sum(elves[:3]))                       # part 2