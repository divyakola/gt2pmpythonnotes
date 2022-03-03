num=int(input("enter your number: "))
s=0
i=1
while i<num:
    if num%i==0:
        s+=i
    i+=1
if num==s:
    print("Given number is a perfect number")
else:
    print("Given number is not a perfect number")
