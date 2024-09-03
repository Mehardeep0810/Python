import math
raw_list = []
print('=============')
print("Enter 10 numbers : ")
for i in range(0,10):
    raw_list.append(int(input()))
square = [x**2 for x in raw_list]
fact = [math.factorial(x) for x in raw_list]

print("Square list: ",square)
print("Factorial list: ",fact)
print('=============')
