print("===================================")
names=['Mehar','Raj','Sia','Swati','Mehar','Palak','Sia','Simran','Raj','Swati']
duplicate=[]
for name in names:
    if names.count(name)>1 and name not in duplicate:
        duplicate.append(name)
        print(name)
        positions = [i for i, x in enumerate(names) if x == name]
        for pos in positions:
            print('\t',pos,end=' ')
        print()
print("================================")
