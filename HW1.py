"""
Molly Donnellan U8754-7477
Hassan Zaidi U2548-2986
"""

#opens the file inputHW1.txt and appends the contnents to the list values
def read():
    file = open("inputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values
   
#finds the minimum value of an array
def min(values = read()):
    min = values[0]
    #iterates through the array, if the value at index i is less than the minimum value it becomes the new min
    for i in range(len(values)):
        if values[i] < min:
            min = values[i]
    return min

#finds the maximum value of an array
def max(values = read()):
    max = values[0]
    #iterates through the array, if the value at index i is greater than the maximum value it becomes the new max
    for i in range(len(values)):
        if values[i] > max:
            max = values[i]
    return max

#assigns variables to both functions
minVar = min()
maxVar = max()

#prints the minimum and maximum values of each function
print("Maximum value: ", maxVar)
print("Minimum value: ", minVar)