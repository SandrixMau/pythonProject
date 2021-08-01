# In order to change the data in lists we can also use builds in python methods.
# Methods are specific kind of functions, they look and behave like functions but their
# behaviour is a bit different. A function acts on its own, a method it’s own by the data that it works for.
# The list methods are a way to manipulate the lists that are involve in.

# FUNCTIONS: print(), len(), input()
# METHODS: list.append(), list.insert()

# With append we can add a new item to the end of the list.
# With the insert we can add an item in between values.

countries = ["USA", "Canada", "India"]
countries.append("Spain")
countries.insert(2, "Italy")
print(countries)
# We can move items by creating a temporary variable:
countries = ["USA", "Canada", "India"]
temp = countries[0]
countries[0] = countries[1]
countries[1] = temp
print(temp)

# However there is an easier way to do this, we are saying that the 1st value on the list
# should have the 2nd value, and the second value should have the 1st one on the list:
countries = ["USA", "Canada", "India"]
countries[0], countries[1] = countries[1], countries[0]
print(countries)

# Sort: It sorts from lower to higher or from the 1st to the last letter of the alphabet

ages = [56, 72, 24, 46]
ages.sort()
print(ages)

# Reverse: it sorts them from higher to lower

ages.reverse()
print(ages)
