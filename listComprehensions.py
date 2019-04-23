x = range(10)
out = [num ** 2 for num in x]
print(out)

# Labmda function to create fucntion in shorter sentex


def newFun(var): return var**2


print(newFun(5))

# Map to call a fucntion multiple times dont forgot to wrap it into a list
numbers = list(range(1, 15))
newlist = list(map(newFun, numbers))
print(newlist)
# You can directly use lambda in map to save memory
newList2 = list(map(lambda num: num**3, numbers))
print(newList2)
# Filter return bollen value if true it save that value just like javascript
print(list(filter(lambda num: num % 2 == 0, numbers)))

sen = "Hi there my  name is najam"
print(sen.split("m")[1])
