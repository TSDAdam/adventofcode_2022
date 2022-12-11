with open ('./11.in') as file:
    data = [line.strip() for line in file]


def getMonkeys():
    monkeys = {}
    i = 0
    while True:
        id = int(data[i].split(" ")[1][0])
        monkeys[id] = {}
        monkeys[id]["inspected"] =0
        i += 1
        items = data[i][data[i].find(":") + 2:]
        monkeys[id]["items"] = []
        for item in items.split(", "):
            monkeys[id]["items"].append(int(item))
        i += 1
        monkeys[id]["operation"] = data[i][data[i].find("old")+4:]
        i += 1
        monkeys[id]["test"] = int(data[i][data[i].rfind(" ") + 1:])
        i += 1
        monkeys[id]["throwiftrue"] = int(data[i].split(" ")[-1])
        i += 1
        monkeys[id]["throwiffalse"] = int(data[i].split(" ")[-1])
        i += 1
        if i >= len(data):
            break
        else: 
            i += 1
            continue
    return monkeys

def newvalue(current, op, val):
    if val == 'old':
        val = current
    val = int(val)
    if op == "+":
        return ((current + val) // 3)
    elif op == "*":
        return ((current * val) // 3)


def modvalue(current, op, val, supermod):
    if val == 'old':
        val = current
    val = int(val)
    val %= supermod
    if op == "+":
        return (current + val)
    elif op == "*":
        return (current * val)

# Part 1 

monkeys = getMonkeys()

for _ in range(20):
    for i in range(len(monkeys)):
        newitems = []
        op, val = monkeys[i]["operation"].split(" ")
        for item in monkeys[i]["items"]:
            newitems.append(newvalue(item, op,val))
            monkeys[i]["inspected"] += 1
        truemonkey = monkeys[i]["throwiftrue"]
        falsemonkey = monkeys[i]["throwiffalse"]
        for item in newitems:
            if item % monkeys[i]["test"] == 0:
                monkeys[truemonkey]["items"].append(item)
            else:
                monkeys[falsemonkey]["items"].append(item)
        monkeys[i]["items"] = []

inspections = []        
for i in range(len(monkeys)):
    inspections.append(monkeys[i]["inspected"])
print("Part 1: {}".format(sorted(inspections, reverse=True)[0] * sorted(inspections, reverse=True)[1]))


# PART 2
supermod = 1

for i in range(len(monkeys)):
    supermod *= monkeys[i]["test"]

monkeys = getMonkeys()
for _ in range(10000):    
    for i in range(len(monkeys)):    
        newitems = []
        op, val = monkeys[i]["operation"].split(" ")
        for item in monkeys[i]["items"]:
            newitems.append(modvalue(item, op,val, supermod))
            monkeys[i]["inspected"] += 1
        truemonkey = monkeys[i]["throwiftrue"]
        falsemonkey = monkeys[i]["throwiffalse"]
        for item in newitems:
            if item % monkeys[i]["test"] == 0:
                monkeys[truemonkey]["items"].append(item)
            else:
                monkeys[falsemonkey]["items"].append(item)
        monkeys[i]["items"] = []


inspections = []        
for i in range(len(monkeys)):
    inspections.append(monkeys[i]["inspected"])
print("Part 2: {}".format(sorted(inspections, reverse=True)[0] * sorted(inspections, reverse=True)[1]))