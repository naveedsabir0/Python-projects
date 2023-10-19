n1=(input("enter the first number: "))
n2=(input("enter the second number: "))
s=(input("""WELCOME!!
1. addition
2. subtraction
3. multiplication
4. division
5. raise
6. modulus
choice:  """))

def addition():
    result=float(n1)+float(n2)
    print(result)

def substraction():
    result=float(n1)-float(n2)
    print(result)

def multiplication():
    result=float(n1)*float(n2)
    print(result)

def division():
    result=float(n1)/float(n2)
    print(result)

def raiser():
    result=int(n1)**int(n2)
    print(result)

def modulus():
    result=float(n1)%float(n2)
    print(result)

if s=='1':
    addition()
elif s=='2':
    substraction()
elif s=='3':
    multiplication()
elif s=='4':
    division()
elif s=='5':
    raiser()
elif s=='6':
    modulus()
else:
    print("Wrong input")