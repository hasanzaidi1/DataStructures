
print("\nrevision basic python")

intNum = int(23.99)
floatNum = float(22.999999999)

print(intNum, floatNum)
print(intNum, int(floatNum))

#logical 

print()
print(False and False)
print(True and False)
print(True or False)
print(not False)
print()


#Bitwise operators
print(4 << 2) # 4 / 2^2 = 16
print(128 >> 4) # 128 / 2^4 = 8
print("")
print(0b1111 & 0b1100) # = 0b1100 = 12    and
print(0b1111 | 0b1100) # = 0b1111 = 15    or
print(0b1111 ^ 0b0110) # = 0b1001 = 9     xor - if both are SAME it is 0 if both are DIFFERENT it is 1


print("")
# if statements 
number = 3
if number % 2 == 0:
    print("even")
else: 
    print("odd")


# Reading input from a User
name = input("Enter your name: ")
age = input("Enter age: ")
salary = int(input("Enter salary: "))  # if we want to manipulate a number after; Do casting for it


bonus = 100

salary = salary + bonus

print(salary)


print("")
# lists
myList = []
otherList = list()

myList.append(10)
otherList.append(40)

myList[0] = 2990

myList.append('kjsahdb')

otherList.append('uhsd21')

print(myList, otherList)


names = 'john, ahsdb,   ahsbd, ajshb'

print(names.split(','))


print("\n")
