# How to use while loop python same as javscript
num = 0
newname,newage = "woww",55
print(newage)
print(newname) 
while num < 10:
    print("hello")
    num += 1


class Person:
    def __init__(self, fullName):  # this is class constructor
        self.name = fullName  # self is like "this" of javascript
    def nameofPerson(self):
        print(self.name)


najam = Person("Najam Shehzad Butt")
najam.nameofPerson()

# It also pass referanc just like javascript
newMember = najam
print(newMember.name)
najam.name = "Najam"
print(newMember.name)
a = 55
b = a
print(b)
a = 70
print(b)
print(a)
import sys
numberVar = 5;
print(sys.getsizeof(5))
