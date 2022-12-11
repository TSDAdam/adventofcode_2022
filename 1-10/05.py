from copy import deepcopy

with open ('./05.in') as file:
    data = [line for line in file]

# Right, let's parse this b*tch
rawStacks = []
stacks = []
for _ in range(0,8):
    rawStacks.append(list())
for _ in range(0,9):
    stacks.append(list())

for x, row in enumerate(data[0:8]): # this loop mirrors the visual style of crates from input. Not good for looping through
    for i in range(0, len(data[0]), 4):
        rawStacks[x].append(row[i:i+3])

for y in range(len(rawStacks)-1, -1 ,-1): # this loop transposes the crates list above, so each list contains a stack
    for i, crate in enumerate(rawStacks[y]):
        if " " not in crate:
            stacks[i].append(crate)

stacksCopy = deepcopy(stacks) # this bit is SUPER important. If you use x=y with a list, you make a copy of the list
                              # as a reference. So when y changes, x does too. deepcopy makes a non-referential copy
instructions = []
for row in data[10:]:
    details = row.strip().split(' ')
    instructions.append([int(details[1]), int(details[3]), int(details[5])])
    # Reminder for me: first is multiplier, second is from stack, third is to stack

# PART ONE

for instruction in instructions:
    steps = instruction[0]
    fromStack = instruction[1] -1                       # instructions aren't zero-index, lists are
    toStack = instruction[2] -1
    for _ in range(steps):
        stacks[toStack].append(stacks[fromStack].pop()) # pop the crates off one at a time and add to new stack

ans = ''
for stack in stacks:
    ans += stack[-1][1]
print(ans)

# PART TWO

for instruction in instructions:
    steps = instruction[0]
    fromStack = instruction[1] -1
    toStack = instruction[2] -1
    crateStack = []
    for _ in range(steps):
        crateStack.append(stacksCopy[fromStack].pop())  # pop those crates off into a temporary stack
    for c in reversed(crateStack):                      # reverse that temp stack, so it's the right way up
        stacksCopy[toStack].append(c)                   # and add them one at a time to the new stack

ans2 = ''
for stack in stacksCopy:
    ans2 += stack[-1][1]
print(ans2)