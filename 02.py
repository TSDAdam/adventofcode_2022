with open ('./02.in') as file:
    data = file.read().split('\n')[:-1]

wintable = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B'
}

drawtable = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'   
}

guessvalues = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
score = 0
WIN = 6
DRAW = 3

for row in data:
    myguess = row[2]
    theirguess = row[0]
    if theirguess == drawtable[myguess]:
        score += (DRAW + guessvalues[myguess])
        print('draw')
    elif wintable[myguess] == theirguess:
        score += (WIN + guessvalues[myguess])
        print('win')
    else:
        score += guessvalues[myguess]
        print('lose')
print(score)