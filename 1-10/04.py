with open ('./04.in') as file:
    data = [line.strip() for line in file]

count = 0
count2 = 0

# PART ONE
for row in data:
    a1, a2 = row.split(',')
    min1, max1 = map(int, a1.split('-'))
    min2, max2 = map(int, a2.split('-'))
    elf1 = range(min1, max1)
    elf2 = range(min2, max2)
    if (elf2.start >= elf1.start and elf2.stop <= elf1.stop) or (elf1.start >= elf2.start and elf1.stop <= elf2.stop): 
        count += 1 # check if one range is completely inside the other

# PART TWO        
    if elf1.start <= elf2.stop and elf2.start <= elf1.stop: # just checking for any overlap for part two
        count2 += 1

print(count)
print(count2)