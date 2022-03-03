num=int(input("enter your number: "))
no_of_digits=len(str(num))
temp=num
s=0
while temp>=1:
    dig=temp%10
    s+=dig**no_of_digits #s=s+dig**no_of_digits
    temp//=10 #temp=temp//10
if num==s:
    print("Given number is a Armstrong number")
else:
    print("Given number is not a Armstrong number")
