# Find an item in the list

letters = ["A", "B", "C", "D", "E"]
print("B" in letters)

# Find if an item is not in the list
print("Z" not in letters)

# Nested lists.
# The elements of a list can also be another list.
# The following is called a matrix (a list that exists on another list)
# So the first value represents the row, and the second one the index:

classroom = [
    ["Sam", "Max", "Joe", "Sally"],
    ["Sam", "Max", "Randy", "Linda"],

]
student = classroom[1][3]
print(student)

# Nested list 3D

school = [
  [
    ["Sam", "Max", "Joe", "Sally"],
    ["Sam", "Max", "Randy", "Linda"],
  ],
  [
        ["Sam", "Max", "Joe", "Sally"],
        ["Sam", "Max", "Randy", "Linda"],
  ],
]
print(school[0][1][2])