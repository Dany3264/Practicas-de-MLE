#4-10 Slices: Using one of the programs you wrote in this chapter, add several
#lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to
#print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Use a slice to
#print three items from the middle of the list.
#• Print the message The last three items in the list are:. Use a slice to print the
#last three items in the list.

players = ["Juan", "miguel", "orlando", "daniel", "Carlos", "josé", "christian", "isai", "alfredo"]

print(f"The first three items of the list are: \t\n{players[0:3]}")
print(f"Three items form the middle og the list are: \t\n{players[3:6]}")
print(f"The last three items of the list are: \t\n{players[6:9]}")

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
#(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
#Then, do the following:
#Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite
#pizzas are:, and then use a for loop to print the first list. Print the message
#My friend’s favorite pizzas are:, and then use a for loop to print the second
#list. Make sure each new pizza is stored in the appropriate list.


pizzas = ["Italian", "Margerita", "Brocoli"]

friend_pizzas = pizzas[:]
friend_pizzas.append("Napolitan")

print("My favorite pizzas are:")
for pizza1 in pizzas:
	print(pizza1)

print("my firend´s favourite pizzas are:")
for pizza2 in friend_pizzas:
	print(pizza2)

	