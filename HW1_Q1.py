
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
        else:
            continue
        return min

def max(values = read()):
    max = values[0]
    for i in range(len(values)):
        if values[i] > max:
            max = values[i]
        else:
            continue
        return max


def Trendchange(values = read()):
    change = list()
    num = values[0]
    for i in values:
        for x in values[1:]:
            if i < x:
                print("asc")
            if i > x:
                print("dec")

trend = Trendchange()
minVar = min()
maxVar = max()

# print(trend)
print(minVar)
print(maxVar)
