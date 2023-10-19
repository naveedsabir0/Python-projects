def check_continue ():                                                      # first of all we create a funciton to check if the user wants to continue or not.
    quit=input('To exit please insert Y/N: ')                               # this command creates the variable which will ask the user at the end of the main progrm to exit or not.
    if quit =="Y" or quit == "y":                                           # if the user enters y or Y the value of x will become True. (later on will explain the importance of x)
        x=True
        
    elif quit == "N" or quit =="n":                                         # and if the user decides to continue, he will need to press the n key in upper case or lower.
        x=False                                                             # this will make the x to be False.
    
    return x                                                                # and the function returns the value of x

def check_numeric(n):                                                       # here we define a funtion named check_numeric, this is used to check if the rate and hours inserted are correct values or not.
    while n.isnumeric() == False:                                           # when the number inserted is not a integer, the program will ask to enter the value again and again.
        n = (input('You did not inserted a number, enter again: '))         
    if n.isnumeric()==True:                                                 # but in case the value is numerical, then the function will return the same value in float numbers.
        num = float(n)
        return num

def computepay(hours,rate):                                                 # This function calculates the pay after receiving two values,hours and rate.
    if rate == 0 or rate=="":                                                           # if the rate we enter is 0, the default rate will be £10/hour
        if hours <=40:                                                      # if the hours worked are less than 40, then the pay will be hours * rate
            pay = hours * 10                                                
        elif hours >40:                                                     # and if the hours worked are above than 40, then the pay will be 40 * rate + the extra hours * rate * 1.5
            pay = (40*10) + ((hours-40)*1.5*10)
    else:                                                                   # here is the same as above, but the difference is that here the user has indicated the pay rate.
        if hours <= 40:
            pay = hours * (rate/100)
        elif hours > 40:
            pay = (40*(rate/100)) + ((hours-40)*1.5*(rate/100))
        
    print('Your pay is:',"£" '{:,.2f}'.format(pay))                         # finally the function will print out the pay of the user

# MAIN PROGRAM
f=False                                                                     # the f here is the x value which we used in the first function.
while f == False:                                                           # while f is false, the program will keep running.
    hours = input('Please insert the number of hours worked: ')             # the user must enter the hours worked, and then it calls the function check numeric, to check if the value
    hours2 = check_numeric(hours)                                           # entered is in a correct format or not.
    rate = input('Insert the pay rate in pence p (Optional): ')             # the same happens with the pay rate.
    rate2 = check_numeric(rate)
    
    computepay(hours2,rate2)                                                # here we call the function which compute the pay, with the previous values inserted of hours and rate.
    
    f = check_continue()                                                    # and finally the program calls the function check continue, to check if the user wants to continue or to quit.
 