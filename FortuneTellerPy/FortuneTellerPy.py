def quitter(input):
    if input.lower() == "quit":
        exit()

#Part one - Copy and prompt
print("I'm a fortune teller, of sorts.")
first_name = input("What's your first name?\n")
quitter(first_name)
print()
last_name = input("Good! Your last name?\n")
quitter(last_name)
print()
age = input("And your age?\n")
quitter(age)
print()
print("You don't say! And what's your birth month (by number)?")
birth_month = input("Like '1' for January, and so on.\n")
quitter(birth_month)
print()
print("What is your favorite ROYGBIV color?")
favorite_color = input("I can help if you type 'help'.\n")
print()
while favorite_color == "help":
    #help prompt for favorite colors, with extra prompt
    print("R = Red")
    print("O = Orange")
    print("Y = Yellow")
    print("G = Green")
    print("B = Blue")
    print("I = Indigo")
    print("V = Violet")
    print()
    favorite_color = input("What is your favorite ROYGBIV color?\n")
quitter(favorite_color)
num_sibs = input("Okay, you are a trooper. One last question: how many siblings do you have?\n")
quitter(num_sibs)
print()








