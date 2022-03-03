x=int(input("enter x value: "))
y=int(input("enter y value: "))
z=int(input("enter z value: "))
if x>y and x>z:
    print("x is a maximum number")
elif x==y==z:
    print("all are equal numbers")
elif x==y and z<x:
    print("x and y are the maximum numbers")
elif x==z and y<x:
    print("x and z are the maximum numbers")
elif y==z and x<y:
    print("y and z are the maximum numbers")
elif y>z:
    print("y is a maximum number")
else:
    print("z is a maximum number")
