age = int(input("Enter age : "))
print("\t\t\t\t NOTE: Only \'wednesday\' having discount offer ")

day = input("Enter Day Name: ").lower()

days_names=["Sunday","monday","tuesday","wednesday","thursday","friday","Saturday"]

print("-"*60)

if day not in days_names:
    raise ValueError 
else:
    print("Today is {}".format(day))

price = 12 if age >= 18  else 8

if day == 'wednesday':
    price = price - 2

print("YOUR Ticket price is {}".format(price))    