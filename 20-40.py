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

for valueOfKey in person.values():  # to print the Value of keys
    print(valueOfKey)


for valueOfKey in person.keys():  # to print the Keys of the values
    print(valueOfKey)

for eachKey, eachValue in person.items():  # To print both key and value we use this
    print("The key is " + str(eachKey) + " and the value is " + str(eachValue))


#  List of Dictionaries aka Array of object same sas Javascript object and array
arrayOfObjects = [
    {
        "name": "najam",
        "age": 21
    },
    {
        "name": "ali",
        "age": 20
    }
]
print(arrayOfObjects)

# object containing array
arrayOfObjects.append({"numbers": [5555.54, 54, 53, 77]})
print(arrayOfObjects)

# You can also create object of objects

objectOfObjects = {
    0:{
        "name": "Najam Shehzad Butt",
        "age": "21",
    },
    1:{
        "name": "Najam Shehzad",
        "age": "22",
    },
}
print(objectOfObjects)