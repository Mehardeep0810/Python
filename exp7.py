sn=["Mehar","Swati","Sneha","Kartik","Vanshika","Drishti","Joy","Joe","Jaspreet","Bhagya","Ritvik","Talveen","Simran","Ram","Riya"]
sv=int(input("Enter the starting index: "))
ev=int(input("Enter the ending index: "))
sliced_sn=sn[sv:ev]
print("Sliced elements: ")
for i in sliced_sn:
    print(i,len(i))
