s=input("enter your string: ")
if s.isalpha():
    if s.islower():
        print("Given string object contains only lowercase\
 alphabets")
    elif s.isupper():
        print("Given string object contains only upperrcase\
 alphabets")
    else:
        print("Given string object contains both lowercase\
 and uppercase alphabets")
else:
    print("Given string object contains not only alphabets")
        
