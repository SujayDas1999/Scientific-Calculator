def add(a,b):
    ''' It adds two number'''
    return a+b
def sub(a,b):
    ''' It substracts two number'''
    return a-b
def mul(a,b):
    '''It multiplies two number'''
    return a*b
def div(a,b):
    '''It divides two number'''
    return a/b

print("Enter your choice")
print("Press 1 for addition")
print("Press 2 for Substraction")
print("Press 3 for Multiplication")
print("Print 4 for Division")

choice = int(input("Enter your choice"))
num1 = int(input("Enter your first number"))
num2 = int(input("Enter your second number"))

if choice == 1:
    print("The addition of {0} and {1} is = {2}".format(num1,num2,add(num1,num2)))
elif choice == 2:
    print("The substraction of {0} and {1} is = {2}".format(num1,num2,sub(num1,num2)))
elif choice == 3:
    print("The multiplication of {0} and {1} is {2}".format(num1,num2,mul(num1,num2)))
elif choice == 4:
    print("{0} divides {1} and the reminder is {2}".format(num1,num2,div(num1,num2)))
else:
    print("You have entered an invalid character")