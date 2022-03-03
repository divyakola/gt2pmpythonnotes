s=input("enter your string: ").casefold()
if s==s[::-1]:
    print("Given string is Palindrom string")
else:
    print("Given string is not a Palindrom string")
