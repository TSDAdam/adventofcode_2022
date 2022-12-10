from collections import deque

with open ('./10a.in') as file:
    data = deque(line.strip() for line in file)

cycle = 0
register = 1
regValues = []

while len(data) > 0:
    cmd = data[0][:4]
    regValues.append(register)
    cycle += 1
    if cmd == "addx":
        regValues.append(register)
        cycle += 1
        val = int(data[0].split()[1])
        register += val

    data.popleft()

p1 = 0
for i in range(19, len(regValues), 40):
    p1 += ((i + 1) * regValues[i])
print (p1)

# PART 2
CRT = []
i = 0
for y in range(6):
    string = ""
    for x in range(40):
        if regValues[i] in range(x - 1, x + 2):
            string += "#"
        else:
            string += "."
        i += 1
    CRT.append(string)

for s in CRT:
    print(s)
