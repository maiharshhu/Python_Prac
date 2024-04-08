valid_inp = ["green","yellow","brown"]

user_inp = input("Enter Colour of Banana\'(Green, Yellow, Brown)\' :").lower()
print("-"*55)

if user_inp not in valid_inp:
    print("YOU ENTERED WRONG INPUT")

else:
    if user_inp == 'green':
        print("Banana is Unripe")

    elif user_inp == 'yellow':
        print("Banana is Ripe")

    else:
        print("Banana is Overripe")

