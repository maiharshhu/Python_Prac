# creating a valid list of available options
weather_opt = ["sunny","rainy","snowy"]

# Take input from user
user_inp = input("Enter weather Condition\'[Sunny,Rainy,Snowy]\': ").lower()

print("-"*60)
# checking condition for weather 
if user_inp not in weather_opt:
    print("YOU ENTERED WRONG INPUT")
else:
    if user_inp == 'sunny':
        print("Go for a Walk")

    elif user_inp == 'rainy':
        print("Read a book")

    else:
        print("Build a snowman")
