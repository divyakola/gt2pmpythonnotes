print("Choose any one Option from the following options:\n\t\
1).Domestic\n\t2).Industrial")
option=int(input("enter your option: "))
if option==1:
    units=int(input("enter meter reading units: "))
    if units<=50:
        cost=units*3
        print("Total Charge is %.2fRs"%cost)
    elif units>50 and units<=100:
        cost=50*3+(units-50)*5
        print("Total Charge is %.2fRs"%cost)
    elif units>100 and units<=150:
        cost=50*3+50*5+(units-100)*7.5
        print("Total Charge is %.2fRs"%cost)
    elif units>150 and units<=200:
        cost=50*3+50*5+50*7.5+(units-150)*9
        print("Total Charge is %.2fRs"%cost)
    else:
        cost=50*3+50*5+50*7.5+50*9+(units-200)*11
        print("Total Charge is %.2fRs"%cost)
else:
    units=int(input("enter meter reading units: "))
    if units<=50:
        cost=units*5
        print("Total Charge is %.2fRs"%cost)
    elif units>50 and units<=100:
        cost=50*5+(units-50)*7
        print("Total Charge is %.2fRs"%cost)
    elif units>100 and units<=150:
        cost=50*5+50*7+(units-100)*9.5
        print("Total Charge is %.2fRs"%cost)
    elif units>150 and units<=200:
        cost=50*5+50*7+50*9.5+(units-150)*11
        print("Total Charge is %.2fRs"%cost)
    else:
        cost=50*5+50*7+50*9.5+50*11+(units-200)*13
        print("Total Charge is %.2fRs"%cost)
    
print("Thank you")
        
