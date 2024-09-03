dict={}
for i in range(20):
    print("=================================")
    phone_no=input("Enter your Phone Number : ")
    name=input("Enter your Name : ")
    if len(phone_no)!=10 or phone_no =="":
        print("Please Enter the Correct Phone Number")
        continue
    dict[phone_no] = name
print("===================================")
find = input("Enter the Number you want to Search : ")
if find in dict.keys():
    print(find + " -> "+dict[find])
else:
    print("NUmber not found")
    
