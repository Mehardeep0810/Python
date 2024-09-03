print("Mehardeep Kaur")
print("2210997287")
name=input("Enter the string value: ");
count=len(name)
for i in range (0,count):
    for j in range(0,i+1):
        print(name[j],end='')
    print("\n")


