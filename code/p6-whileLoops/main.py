print("What's your name?")
name = input("> ")

while name != "Bob":
    print("I don't know you...")
    print("What was your name again?")
    name = input("> ")

print("Hi " + name)
