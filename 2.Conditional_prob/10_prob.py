pet_type = input("Enter pet Name [Cat or Dog]: ").lower()

age = int(input("Enter pet age: "))

print("-"*60)

if (pet_type == "dog" and age < 2):
    print("Puppy food")

elif (pet_type == "cat" and age>5):
    print("Senior cat food")
    
else:
    print("Sorry Information is not available")