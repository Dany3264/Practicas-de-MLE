toppings = ("Pepperoni", "Pineapple", "Peppers", "Chicken", "Cheese")
pizza = []
while True:
    ingridients = input("What ingredient would you like?: ").strip().title()
    if ingridients == "Finish":
        break
    elif ingridients not in toppings:
        print("We don't have that ingridient")
    else:
        added_ingridient = ingridients
        pizza.append(added_ingridient)
        print(f"{ingridients} added to your order!")
        if ingridients == "Finish":
            break
    continue

print(f" preparing your pizza with the next toppings: {pizza}")