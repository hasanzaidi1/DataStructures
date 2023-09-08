

def read():
    file = open("inputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values
   

def min(values = read()):
    min = values[0]
    for i in range(len(values)):
        if values[i] < min:
            min = values[i]
    return min

def max(values = read()):
    max = values[0]
    for i in range(len(values)):
        if values[i] > max:
            max = values[i]
    return max

minVar = min()
maxVar = max()

print(minVar)
print(maxVar)
