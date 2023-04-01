sandwiches_orders = ["Pastrami", "4 Cheese", "Pastrami", "Meats", "Pastrami"]
finished_sandwiches = []

while sandwiches_orders:
    sandwich_done = sandwiches_orders.pop()
    print(f"\nI made you a {sandwich_done} sandwich!")
    finished_sandwiches.append(sandwich_done)
    finished_sandwiches.append(sandwich_done)
print(f"\tSandwiches served: \t\n{finished_sandwiches}")

while "Pastrami" in finished_sandwiches:
    finished_sandwiches.remove("Pastrami")
print("\nSorry, we just run out of pastrami!")
