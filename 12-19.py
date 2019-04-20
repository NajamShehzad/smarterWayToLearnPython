#  And and or operator

if 4 > 2 and 5 > 6:
    print("first contdition")

if 5 == 7 or "najam" == "najam":
    print("second condition")

# if statment nested

if 1 == 1:
    if 5 != 5:
        print("najam here")
    else:
        print("nested else")

# List in python aka array

numbers = [5, 4, 5, 7, 48, 45]
print(numbers)
print(numbers[5])
print(numbers.__len__())

# using append aka push in js

numbers.append(88)
print(numbers)
numbers.pop()
print(numbers)
numbers.insert(2, 555)
print(numbers)

# slice in python

# first is the starting index and second is the ednignindex
newArray = numbers[2:5]
print(newArray)

#  delete from array just like delete in javascript

del numbers[0]
print(numbers)
numbers.remove(48) # delete using value
print(numbers.pop()) 

