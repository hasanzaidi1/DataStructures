"""
Molly Donnellan U8754-7477
Hassan Zaidi U2548-2986
"""

#imports the matplotlab library
import matplotlib.pyplot as plt

#opens the file inputHW1.txt and appends the contnents to the list values
def read():
    file = open("inputHW1.txt", "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values
   
#identifies trend points of an array
def Trendchange(values = read()):
    #initializes an array to append the trendpoints to
    change = list()
    #iterates through the array, 
    #if the value at the current index is less than the next one yet greater than the previous it appends the next two indexes
    #if the value at the current index is greater than the next one yet less than the previous it appends the next two indexes
    for i in range(len(values) - 2):
        if((values[i] > values[i+1] & values[i+1] < values[i+2]) | (values[i] < values[i+1] & values[i+1] > values[i+2])):
                change.append(values[i+1])
                change.append(values[i+2])
    #changes the list to a set to get rid of any repeated values
    change = list(set(change))
    return change

#initializes the function Trendchange() to trends and prints it
trends = Trendchange()
print("Trend change points: ", trends)

#plots the result of trends and shows the result
plt.plot(trends)
plt.show()
