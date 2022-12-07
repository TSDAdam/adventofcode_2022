with open ('./07x.in') as file:
    data = [line.strip() for line in file]

dirs = {"/": ""}

def ls(contents):
    return


i = 0
text, values = data[i].split(" ")
if text == "$":
    command, arg = values.split(" ")
    if command == "cd":
        pwd = arg 

elif text == 