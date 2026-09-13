name = input("What's your name?")
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print("1) About me")
    print("2) My Goals")
    print("3) Exit")
    choice = input("Pick 1 - 3")
    if choice == "1":
        print("I am a 15 year old sophmore in highschool. i like to read and paint.")
    elif choice == "2":
        print("Be better at art and school and become a doctor")
    elif choice == "3":
        print("Goodbye!")
        running = False
    else:
        print("Pick 1, 2, or 3.")