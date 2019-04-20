# Defining function in Python
def cube(number):  # passing argument to function
    print(number * number)
    return number * number * number


def addTwoNumbers(num1=5, num2=8):  # Default perameter
    print(num1+num2)
    return num1 + num2


print(cube(5))
print(addTwoNumbers(num2=5))  # passing value to specific paremeter


# it store all the other arguments in a dictionary/ Object
def addNumberAsMuchAsYouwant(name, **numbers):
    finalNumber = 0 #This is local variable 
    for num in numbers.values():
        finalNumber += num
    print(finalNumber)
    addTwoNumbers(5,7) #this fucntion will not have finalNumber is its scope
    print(name)
    return finalNumber + 8 #reutn anything you want object array number string

number122 = 88 #this si global vairable

print(addNumberAsMuchAsYouwant("najam", num1=58, num2=44))
