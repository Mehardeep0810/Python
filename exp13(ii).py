arr=[[1,2,3],[4,5,6],[7,8,9]]
print('====================')
print("Sum of Each Row : ")
for i in arr:
    total=sum(i)
    print(total, end=' ')
print("\nSum of Each column : ")
for i in range(len(arr[0])):
    total=0
    for j in range(len(arr)):
        total+=arr[j][i]
    print(total, end=' ')
print('\n==================')
