# Take input from user 
age = int(input("Please enter age: "))

# now checking condition for child, teenager, Adult, senior
if age<=110:
    if age<13:
        print("Child")

    elif age<20:
        print("Teenager")

    elif age<60:
        print("Adult")

    else:
        print("Senior Citizen")

else:
    print("you enter wrong input")

print("Thank you so much for using this program \n Have a great day")