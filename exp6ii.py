def abc(*args,**kwargs):
    print("value using *: ")
    print(args)
    print("value using **: ")
    for i in kwargs.items():
        print(kwargs)

x=2
y=3
z=4

abc(x,y,z,a=2,b=3,c=4)
