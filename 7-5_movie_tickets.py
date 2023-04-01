ticket_prices = ("Free!", "$10.00", "15.00")
age = int(input("How old are you?: "))

if age < 3:
    print(f"Price is: {ticket_prices[0]}")
elif age > 3 and age < 13:
    print(f"The price is {ticket_prices[1]}")
elif age > 65:
    print(f"The price is {ticket_prices[0]}")
else:
    print(f"The price is {ticket_prices[2]}")