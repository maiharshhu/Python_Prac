size_choice = input("Please Enter coffee size \'[Small,Medium,Large]\':").lower()


if size_choice == 'small':
    print("You choose small coffee")

elif size_choice == 'medium':
    print("You choose Mediu coffee")

else:
    print("You choose large coffee")

print("-"*60)    

extra_shot = input("Do you need Extra shot:\'(Yes/No)\'").lower()
print("-"*60)  

if extra_shot == 'yes':
    print("Your {} coffee with extra shot is ready".format(size_choice))

elif extra_shot == "no":
    print("Your {} coffee is ready\n".format(size_choice))  

else:
    print("You choose wrong input")

print("="*50) 

print("Thank you so much for using our service!")