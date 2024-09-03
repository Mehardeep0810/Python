mydict={}
for i in range(10):
    print("====================================")
    roll_no=int(input("Enter your Roll No : "))
    name = input("Enter your name : ")
    age = int(input("Enter your Age : "))
    stream = input("Enter your Stream : ")
    contactNo= input("Enter your Contact Number : ")
    mydict[roll_no] = [name,age,stream,contactNo]
    print("====================================")
search = int(input("Enter the Roll_No you want to search: "))
if search in mydict.keys():
    for val in mydict[search]:
        print(val)
else:
    print(str(search)+"Was not Found")
