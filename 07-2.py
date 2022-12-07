
with open ('./07.in') as file:
    data = [line.strip() for line in file]

content = dict({"root": 0})

for row in data:
    if row == "$ cd /":
        currentDir = ["root"]
    elif row[0:7] == "$ cd ..":
        currentDir.pop()
    elif row[0:4] == "$ cd":
        currentDir.append("/".join([currentDir[-1], row[5:]]))
        content[currentDir[-1]] = 0
    elif row[0].isdigit():
        for file in currentDir:
            content[file] += int(row.split(" ")[0])
            #print (content)
p1 = 0
for x in content.values():
    if x <= 100000:
        p1 += x
p2 = []
for y in content.values():
    if y >= content['root'] - 40000000:
        p2.append(y)

print(p1)

print(min(p2))