# Touple immutable list/array
newToupleArray = (10, 57, 11, 33)
print(newToupleArray)
print(newToupleArray.__len__())
# age = int(input("Enter Your age: "))  # Type casting you can use int str,float
# print(age + 5)
name = "naJam"
print(name.upper())  # Change string to upper case
print(name.title())  # change only the first character of word into uppercase
person = {
    "name": "najam",
    "age": 21,
    5: 88
}  # just like object in javascript
print(person)
# how to access that field of object/list also called dictionary in Python
print(person["age"])
print(person[5])  # a number can be a key
person["city"] = "karachi"
print(person)
del person["city"]
print(person)
