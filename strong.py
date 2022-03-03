num=int(input("enter your number: "))
temp=num
s=0
while temp>=1:
    dig=temp%10
    i=1
    f=1
    while i<=dig:
        f*=i
        i+=1
    s+=f
    temp//=10
if num==s:
    print("Given number is strong number")
else:
    print("Given number is not a strong number")
