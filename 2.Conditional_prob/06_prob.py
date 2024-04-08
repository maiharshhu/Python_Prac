usr_inp = int(input("Enter how much KM you want to travel: "))

if usr_inp < 3:
    print("Please choose 'walk' as transport medium")

elif usr_inp < 15:
    print("Please choose 'Bike' as transport medium")

else:
    print("Please choose 'Car' as transport medium")

