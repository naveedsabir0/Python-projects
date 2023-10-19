i='yes'
while i=='yes':
    income=int(input("What's your income? "))
    if income <= 12570:
        print("Tax rate is: 0%")
        taxable_inc=0
        tax=0
        print(f'taxable income after personal allowance: {taxable_inc}')
        print(f'tax: {tax}')
    elif income > 12570 and income <=50270:
        print("Tax rate is: 20%")
        taxable_inc=income-12570
        tax=taxable_inc*(20/100)
        print(f'taxable income after personal allowance: {taxable_inc}')
        print(f'tax: {tax}')
    elif income > 50270 and income <= 150000:
        print("Tax rate is: 40%")
        if income >= 125140:
            taxable_inc=income
            tax=taxable_inc*(40/100)
        else:
            taxable_inc=income-12570
            tax=taxable_inc*(40/100)
        print(f'taxable income after personal allowance: {taxable_inc}')
        print(f'tax: {tax}')
    else:
        print("Tax rate is: 45%")
        taxable_inc=income
        tax=taxable_inc*(45/100)
        print(f'taxable income after personal allowance: {taxable_inc}')
        print(f'tax: {tax}')
    i=str(input("Type 'quit' if you wish to end the program or 'yes' if you wish to conitnue: "))