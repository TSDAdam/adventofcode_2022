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

losetable = {
    'X': 'B',
    'Y': 'C',
    'Z': 'A'   
}

guessvalues = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
}

score = 0
WIN = 6
DRAW = 3


# PART 1
for row in data:                               
    myguess = row[2]                            # split this row into my guess and theirs
    theirguess = row[0]
    if theirguess == drawtable[myguess]:        # is it a draw?
        score += (DRAW + guessvalues[myguess])
    elif wintable[myguess] == theirguess:       # a win?
        score += (WIN + guessvalues[myguess])
    else:                                       # guess not, must be a loss
        score += guessvalues[myguess]
print(score)


# PART 2
score2 = 0

for row in data:
    theirguess = row[0]
    instruction = row[2]
    if instruction == 'X':  
        for k, v in losetable.items():              # use the loss table to find what would have beaten my guess
            if v == theirguess:
                score2 += guessvalues[k]
    elif instruction == 'Y': 
        score2 += guessvalues[theirguess] + DRAW
    else:
        for k, v in wintable.items():
            if v == theirguess:
                score2 += guessvalues[k] + WIN      # use the win table to find out what would have beaten their guess


print(score2)