
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
    
    change = []
    trend_direction = 0 

    for i in range(len(values)-1):

        previous_num = values[i]                # previous num
        current_num = values[i+1]                   # current num

        if current_num > previous_num:
            if trend_direction != 1:
                change.append(values[i])
                trend_direction = 1

        elif current_num < previous_num:
            if trend_direction != -1:
                change.append(values[i])
                trend_direction = -1
        else:
            continue

    return change

        


trend = Trendchange([1, 4, 9, 11, 8, 3, 2, 5, 10])    # 11,8,2,5
minVar = min()
maxVar = max()

print(trend)
print(minVar)
print(maxVar)
