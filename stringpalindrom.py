x=input("enter your string: ")
y=''
s=len(x)-1
while s>=0:
    y+=x[s]
    s-=1
if x==y:
    print("Given string is palindrom string")
else:
    print("Given string is not a palindrom string")
