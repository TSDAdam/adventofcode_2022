pairs = []

with open('advent4input.txt', 'r') as file:
    for line in file.readlines():
        pairs.append(line.strip())

duplicatedWork = 0
crossover = 0

for pair in pairs:
    section = pair.split(',')  # split each line into its 2 pairs
    # split each section into its first value and last value
    firstRange = section[0].split('-')
    # doing the same for the second section
    secondRange = section[1].split('-')
    # create a range for the first section
    firstRange = list(range(int(firstRange[0]), int(firstRange[1])+1))
    # create a range for the second section
    secondRange = list(range(int(secondRange[0]), int(secondRange[1])+1))
    # use intersection to find the matching values between the 2
    matchingValues = list(set(firstRange).intersection(secondRange))
    # check if matching values equals either of the 2 ranges
    if matchingValues == firstRange or matchingValues == secondRange:
        # increase duplicatedWork if its a match
        duplicatedWork += 1
    # part 2 - check for any crossover by ruling out empty matches
    if (len(matchingValues) != 0):
        crossover += 1

print(duplicatedWork)
print(crossover)