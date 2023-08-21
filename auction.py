bidders = {}


def addnew(name, price):
  bidders[name] = price
  
name = input("What is your name ?")
price = input("What is your bid ?")
  
addnew(name, price)

new_bidder = ""
lowest_price = 0

    
def nbidder():
    name = input("What is your name ?")
    price = input("What is your bid ?")
    addnew(name, price)
    new_bidders()

def new_bidders():
    new_bidder = input("Are there other users who want to bid ? y/n")
    if new_bidder.lower() == "y":
        nbidder()
    elif new_bidder.lower() == "n":
        lowest_price = float("inf")
        lowest_bidder = None

        for name, price in bidders.items():
            if int(price) < lowest_price:
                lowest_price = int(price)
                lowest_bidder = name
                print(f"Lowest bid is {lowest_price} by {lowest_bidder}")

new_bidders()
