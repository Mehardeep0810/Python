'''msg1="welcome"
while msg1:
    print (msg1,end='')
    msg1 = msg1[1:]

a=0
b=10
while a<b:
    if(a%2==0):
        print(a, end='')
    a=a+1

x=10
while x>1:
    x=x-1
    if(x==5): break
    print(x, end='')
        
i=0
sum=0
while i<=10:
    sum=sum+4*i
    i=i+1
print(sum)

add=0
for i in range(0,11):
    add=add+4*i
print(add)

n=int(input("Enter the value of table "))
for i in range(1,11):
    print(f'{n}*{i:2}={n*i:3}')

str1 = "ABCDEFGH"
str2 ="ate"
for i in str1:
    print(i+str2,end='\t')

re-> regular expressions

import re

def isvalid(z):
    result=re.compile("[A-Za-z]{4}\d{4}[A-Za-z]{1}")
    return result.match(z)
n=input("Enter you name: ")
z=input("Enter your Pan Card number: ")
if(isvalid(z)):
    print("Pan card is valid") 
else:
    print("Pan card is invalid")'''
'''# Given string and character
s = "Hello, World!"
c = 'o'

# Convert the string to a list of characters
s_list = list(s)

# Check if the character is in the list
if c in s_list:
    # Get the index of the character
    index = s_list.index(c)
    print(f"Character '{c}' found at index {index}")
else:
    print(f"Character '{c}' not found in the string.")

index: exceptional handling is present
find: exceptional handling is not present

#find function
str1=input("Enter a string: ")
str2=input("Enter a string to search ")
search= str1.find(str2)
print("the result is at index",search)'''

str1="This is python class"
c="is"
for i in range(len(str1)):
    if str1[i]==c:
        print(f"The character is found at index {i}")
