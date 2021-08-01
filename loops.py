# if/else statements allow us to conditionally run code
# After the if condition we need to add :, and the next line we need to add a space or a tab
# Always use the same separator
age = int(input("How old are you? "))
if age == 18:
    print("You are 18 years old.")
elif age > 18:
    print("You are old enough!")
else:
    print("You are not old enough!")

# While loop makes it possible to repetitively execute code based on a certain condition.
# Let's guess a number a combine while and if conditions

number = 3
guess = int(input("Guess a number between 0 and 10. "))
while guess != number:
    guess = int(input("Keep trying: "))
else:
    print("Congratulations you got it!")

# We can execute code for each item in a sequence with a for .. in loop
# We can break out of the loop, for ex. When reaching 2 and using the break keyword.
print("1.FOR loop")
for i in range(5):
    if i == 2:
        break
    print("i is: ", i)

# We can skip one iteration, for ex. For 2 nothing will be printed, but it will continue as we added
# the continue keyword:
print("2.FOR loop")
for i in range(5):
    if i == 2:
        continue
    print("i is: ", i)