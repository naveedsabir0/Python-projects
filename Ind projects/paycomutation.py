def check_continue():
    checkContinue = True
    while (checkContinue == True):
            doContinue = input("Enter application? (Type 'Y' for yes and 'N' for no) ")
            if (doContinue.upper() == "Y") :
                checkContinue = False
            elif (doContinue.upper() == "N") :
                checkContinue = False


def check_numeric():
    n = input("Enter a number for 0-9: ")
    while n.isnumeric()==False:
        print("""Wrong input""")
        n = input("Enter a number for 0-9: ")
    print(n)


def computepay(h,r=10):
    h=input("Hours of work: ")
    r=input("Rate of work: ")
    pay=(h*r)
    if h > 40:
        h2=h-40
        r=r*1,5
        pay2=pay+(h2*r)
        print(f'The payment is: {pay2} ')


print("Would you like to calculate your income? ")
while check_continue()=='Y':
    print("Type working hours and rate")
    h=input("Hours of work: ")
    r=input("Rate of work: ")
    print(computepay(h,r))