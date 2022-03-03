num=int(input("enter your number: "))
temp=num
rev=0
while temp>=1:
    dig=temp%10
    rev=rev*10+dig
    temp//=10
if num==rev:
    print("Given number is a Palindrom number")
else:
    print("Given number is not a Palindrom number")
