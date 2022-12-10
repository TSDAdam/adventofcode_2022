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

    
print(regValues)
p1 = 0
for i in range(20, len(regValues), 40):
    print(i , regValues [i], i * regValues[i])
    p1 += (i * regValues[i])
print (p1)