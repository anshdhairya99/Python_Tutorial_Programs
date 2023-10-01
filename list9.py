
# PYTHON LIST AND LIST OF FUNCTION:----------------------------------------------------------

# LIST OF GROCERY USED IN DAILY LIFE:------------------------
grocery = ["Harpic","Egg tray","Chicken","Mutton","fish","Mango juice","Paneer","Lollypop",56]
print(grocery)
print(grocery[5])
numbers = [2,3,4,5,6,7,8,9,10]
print(numbers)
print(numbers[5])

#Sorting the number
numbers.sort()
print(numbers)

#Reverse the numbers
numbers.reverse()
print(numbers)

print(numbers[1:5])
print(numbers)

"""Excluding function and skip function"""
print(numbers[::2])

"""Negative slicing string"""

print(numbers[::-3]) #only take -1
print(numbers[1:5:-3])
print(numbers[1:5:2])

# Used the string
print(len(numbers))
print(min(numbers))
print((max(numbers)))

# Append they are add number behind the integer--
numbers.append(55)
numbers.append(65)
print(numbers)

# Indexing no -
numbers.insert(5,99)
print(numbers)

#remove the number from the table-
numbers = [2,3,4,5,6]
numbers.remove(2)
print(numbers)

# Pop the number fron the table
numbers.pop()
print(numbers)
numbers[1] = 88
print(numbers)

#TUPLES-------------------------------------

#Mutable - Can change.... # Our list is mutable
#Immutable - cannot change..... # Our Tuple is Immutable
tp = (1,2,3,4,5)
print(tp)
tp = (1,)
print(tp)
a=1
b=8
a,b=b,a
print(a,b)