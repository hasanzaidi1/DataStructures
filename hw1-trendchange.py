

def read():
    file = open("inputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values
   

def Trendchange(values = read()):
    change = list()
    for i in range(len(values) - 2):
        if((values[i] > values[i+1] & values[i+1] < values[i+2]) | (values[i] < values[i+1] & values[i+1] > values[i+2])):
                change.append(values[i+1])
                change.append(values[i+2])
    change = list(set(change))
    return change

 
trends = Trendchange()
print("Trend change points: ", trends)
