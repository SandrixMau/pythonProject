# We will create a total variable to store the sum of the values, so we will give them the value of 0.

ages = [56, 72, 24, 46]
total = 0
for age in ages:
    total += age
print("1- ", total)
# Then we will calculate the average using the len

average = total / len(ages)
print("2- ", average)

# There is a difference when working with lists and regular variables, when we define a normal variable Python
# stores the value in memory directly with the string in this case Lidia. When we create a list however we are
# creating a variable which value is simply a reference to the address where that list is stored in memory.
# Whenever we try to create a new variable that should have the same value as the ages variable ,
# for ex. Ages 2. We are actually copying the same spot on memory that ages refers to. This means
# that whenever we change the value of an element of the ages lists, for ex. Changing the first value 56 to 92,
# you also see this change on the ages2 list.

name = "Lydia"
ages = [56, 72, 24, 46]
ages2 = ages
ages[0] = 92
print("3- ", ages2[0])

# If we don't want this to happen we can slice the list.
# Slicing lists
# We can slice lists by using square brackets and specifying an start and end ending. The start element
# will be included in the slice list but not the last one.

letters = ["A", "B", "C", "D", "E"]
firstTwo = letters[0:2]
print("4- ", firstTwo)
print("5- ", letters[1:])
print("6- ", letters[:3])

# We can use negative indexes if we don’t know the exact length of the list. 1:-1 the first and last
# element of the list will be cut off.

print("7- ", letters[1:-1])

# : will print the whole list
print("8- ", letters[:])

# This will print the list backwards
print("9- ", letters[::-1])

# When slicing a list we create a whole new list in memory, this means that if we modify this list we won’t
# modify the original one.
# We can also use del in order to delete a list, however there is a big difference here, where we are creating
# copy when creating a list without indexes, if we delete multiple items by using the del keyword and slicing
# elements we are modifying the original array.

letters = ["A", "B", "C", "D", "E"]
del(letters[1:3])
print("10-", letters)
