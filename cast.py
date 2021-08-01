# The values for the input are always strings, even if the user adds a number.
# So we cannot do arithmetic operations, for that we need to cast the value

age = input("How old are you? ")
print(int(age)-10)

Tocheck:

# If we want to cast a string. print("You are", age), the comma means after the comma we have an int.
# print("You are" + age) age here is expected to be a string. So if needed to be casted.

age = str(input("How old are you? "))
print("Your are" + age)
