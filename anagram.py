s1=input("enter string_1: ").casefold()
s2=input("enter string_2: ").casefold()
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("Given two string objects are Anagram strings")
    else:
        print("Given two string objects are not \
 Anagram strings")
else:
    print("Given two string objects are not Anagram strings")
        
