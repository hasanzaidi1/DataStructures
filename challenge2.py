
fh = open("input.txt","r")

linesOfFile = fh.readlines()

print(linesOfFile)

date = []

for item in linesOfFile:
    print(item.split(",")[2])

print(date)

fh.close()

