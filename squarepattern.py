num=int(input("enter your number: "))
r=0
while r<num:
    c=0
    while c<num:
        if c==0 or c==num-1 or r==0 or r==num-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
        c+=1
    r+=1
    print()
        
