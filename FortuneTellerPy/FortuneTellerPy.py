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
while favorite_color.lower() == "help":
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

#Assignments of Retirement
age = int(age)
if age % 2 == 0:
    years_to_retire = "14"
elif age % 2 == 1:
    years_to_retire = "5"
else:
    years_to_retire = "239,102,839,494,039,392,038,174,777,773,824 (2.39 x 10^32)"

#Vacation Home Assignments
num_sibs = int(num_sibs)
if num_sibs == 0:
    vacation_home = "nowhere special, just Cabo San Lucas"
elif num_sibs == 1:
    vacation_home = "in a Lake Erie undersea palace"
elif num_sibs == 2:
    vacation_home = "on scenic the Moon"
elif num_sibs == 3:
    vacation_home = "of a really big bouncy house"
elif num_sibs > 3:
    vacation_home = "near Sting's house, wherever that is"
else:
    vacation_home = "on a rapidly melting artic glacier"
    
#Mode of transportation assignment
favorite_color = favorite_color.strip().lower()
if (favorite_color == "r" or favorite_color == "red"):
    transit = "rocket boots"
elif (favorite_color == "o" or favorite_color == "orange"):
    transit = "a sweet Caddy"
elif (favorite_color == "y" or favorite_color == "yellow"):
    transit = "some European luxury car"
elif (favorite_color == "g" or favorite_color == "green"):
    transit = "a hanglider"
elif (favorite_color == "b" or favorite_color == "blue"):
    transit = "a flock of cats"
elif (favorite_color == "i" or favorite_color == "indigo"):
    transit = "Santa's sleigh"
elif (favorite_color == "v" or favorite_color == "violet"):
    transit = "an Oldsmobile 88"
else:
    transit = "some beat up Chuck Taylor All Stars"

#Money in bank assignment
birth_month = int(birth_month)
if birth_month >=1 and birth_month < 5:
    money_bank = "100,000.00"
elif birth_month >=5 and birth_month <9:
    money_bank = "200,000.00"
elif birth_month >=9 and birth_month < 13:
    money_bank = "300,000.00"
else:
    money_bank = "0.00"

print("{0} {1} will retire in {2} years with ${3} in the bank, a vacation home {4}, and {5}.".format( first_name, last_name, years_to_retire, money_bank, vacation_home, transit))