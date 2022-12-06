from collections import deque    

with open ('./06.in') as file:
    data = deque(line.strip() for line in file)

string = data[0]
print(string)
lastFour = ""
for i in range(0, len(string)):
    lastFour += string[i]
    if len(lastFour == 4):
        if len(set(lastFour)) == 4:
            print(i)
            break
        else:
