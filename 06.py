from collections import deque    

with open ('./06.in') as file:
    data = [line.strip() for line in file]

string = deque(data[0])

lastFour = ""
for i in range(0, len(string)):
    lastFour = list(string)[:4]
    print(lastFour, set(lastFour))
    if len(set(lastFour)) == 4:  
            print(i + 4)
            break
    else:
        string.rotate(-1)

string = deque(data[0])
lastFourteen = ""
for i in range(0, len(string)):
    lastFourteen = list(string)[:14]
    print(lastFour, set(lastFourteen))
    if len(set(lastFourteen)) == 14:  
            print(i + 14)
            break
    else:
        string.rotate(-1)

