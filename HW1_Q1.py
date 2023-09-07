
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
    
    index = 0

    for i in values[1:]:

        previous_num = values[index]            # first num
        if i < previous_num:                        # second num is less than first num
            # decreasing loop
            # ISSUE : change the continuing range
            for num_dec in values[1:]:                  # a loop for numbers decreasing will initalize
                if num_dec < previous_num:                  # second num is less than first num
                    index = index + 1                           # increment index by 1
                    continue                                    # continue the loop
                else:                                       # else
                    change.append(num_dec)                      # add that number which is changing the trend to list called change
                    break                                       # break the loop after adding that number

        elif i > previous_num:                      # second num is greater than first num
            # increasing loop
            # ISSUE : change the continuing range
            for num_inc in values[:1]:                  # a loop for numbers increasing will initalize
                if num_inc > previous_num:                  # second num is more than first num
                    index = index + 1                           # increment index by 1
                    continue                                    # continue the loop
                else:                                       # else
                    change.append(num_inc)                      # add that number which is changing the trend to list called change
                    break                                       # break the loop after adding that number

        else:                                       # else 
            continue                                    # if both the nums are the same then continue

        

    return change

        


trend = Trendchange()
minVar = min()
maxVar = max()

print(trend)
print(minVar)
print(maxVar)
