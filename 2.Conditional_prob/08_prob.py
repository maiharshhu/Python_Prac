passw = input("Enter password to check strength: ")

if len(passw) < 6:
    print("Your password is weak")

elif len(passw) <=10 :
    print("your password is medium")

else:
    print("your password is strong")
