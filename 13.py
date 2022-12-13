from functools import cmp_to_key

with open ('./13.in') as file:
    data = file.read().strip()
    lines = [line for line in data.split('\n')]



def compare(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return -1
        elif p1 == p2:
            return 0
        else:
            return 1
    elif isinstance(p1, list) and isinstance(p2, list):
        i = 0
        while i < len(p1) and i < len(p2):
            result = compare(p1[i], p2[i])
            if result == -1:
                return -1
            if result == 1:
                return 1
            i += 1
        if i == len(p1) and i < len(p2):
            return -1
        elif i == len(p2) and i < len(p1):
            return 1
        else:
            return 0
    elif isinstance(p1, int) and isinstance(p2, list):
        return compare([p1], p2)
    else:
        return compare(p1, [p2])

datapackets = []
t = 0
for i, pair in enumerate(data.split('\n\n')):
    p1, p2 = pair.split('\n')
    p1 = eval(p1)
    p2 = eval(p2)
    datapackets.append(p1)
    datapackets.append(p2)
    if compare(p1, p2) == -1:
        t += (i + 1)
print(t)

datapackets.append([[2]])
datapackets.append([[6]])

datapackets = sorted(datapackets, key=cmp_to_key(lambda p1, p2: compare(p1, p2)))

t2 = 1
for i, packet in enumerate(datapackets):
    if packet == [[2]] or packet == [[6]]:
        t2 = t2 * (i + 1)
print(t2)