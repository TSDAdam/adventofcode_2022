import string
import time

st = time.time()
with open ('./03.in') as file:
    backpacks = [line.strip() for line in file]

vals = string.ascii_lowercase + string.ascii_uppercase  # handy python shortcut for getting lists of all lower and upper chars
t=0

# PART ONE
for backpack in backpacks:
    sizeOfCompantment = int(len(backpack) / 2)
    compartment1, compartment2 = backpack[sizeOfCompantment:], backpack[:sizeOfCompantment] # split each backpack in two
    common = set(compartment1) & set(compartment2) # set intersections are your friend
    t += vals.find(next(iter(common))) + 1 # just converts the first (only) char in the matching set to a string
print(t)

# PART TWO

t2 = 0
for i in range(0, len(backpacks), 3):
    common = set(backpacks[i]) & set(backpacks[i+1]) & set(backpacks[i+2]) # same thing, just looping three at a time and getting the intersections
    t2 += vals.find(next(iter(common))) + 1
print(t2)

et = time.time()

print (et-st)