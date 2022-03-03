ch=input("enter your charecter: ").casefold()
if ch.isalpha():
    if ch in 'aeiou':
        print("Given alphabet is Vowel")
    else:
        print("Given alphabet is Consonent")
else:
    print("Given charecter is not a Alphabet")
