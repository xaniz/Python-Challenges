#Setting up the inputs required

size = input("Which size do you want? S, M or L\n ")
pepperoni = input("Do you want Pepperoni? Y or N\n ")
extra_cheese = input("Do you want Extra Cheese? Y or N\n ")

#Setting the initial bill to 0
bill = 0

#Getting the input response in order to set a price
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
    
    
#Getting the response if users wants Pepperoni on a small pizza or not
if pepperoni == "Y" and size == "S":
    bill += 2
#Getting the response if users wants Pepperoni on a medium and large pizza or not
elif pepperoni == "Y" and (size == "M" or size == "L"):
    bill += 3

#Getting the response if users wants Extra Cheese or not
if extra_cheese == "Y":
    bill += 1
    

print(f"Your final bill is: ${bill}")




