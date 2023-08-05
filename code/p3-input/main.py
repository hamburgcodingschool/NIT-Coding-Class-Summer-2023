print("What's your name?")
name = input("> ")

print("Hello " + name + ". Good morning. Let's start coding!")

# EXERCISE
# Ask the user for 2 different numbers
# Print the sum of those numbers

print("What's the first number?")
number1 = input("> ") #str
print("What's the second number?")
number2 = input("> ") #str

# converting the number1 to an int
# and then replacing the variable value with the int number
number1 = int(number1)

number2 = int(number2)

sum = number1 + number2
sub = number1 - number2
mult = number1 * number2
divi = number1 / number2
rem = number1 % number2

print(sum)
print(sub)
print(mult)
print(divi)
print(rem)


