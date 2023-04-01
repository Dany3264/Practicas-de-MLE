people = {"Aylin": "Mom",
    "Daniel": "Dad",
    "Elaine": "1st kid",
    "Isaac": "2nd kid",
    "Adeleide": "3rd kid",
    " Liam": "4th kid"}

peoples_friends = {"Aylin's friend": "Daniel",
    "Daniel's friend": "Aylin",
    "Elaine's friend": "Mom",
    "Isaac's friend": "Elaine",
    "Adeleide's friend": "Isaac",
    "Liam's friend": "Isaac"}

peoples_foods ={"Aylin's super": "sweets",
    "Daniel's super": "Breaded chicken",
    "Elaine's super": "Pizza",
    "Isaac's super": "Shrimps",
    "Adeleide's super": "Chicken Nuggets",
    "Liam's super": "Noodles Soup"}

family = [people, peoples_friends, peoples_foods]

for name, title in people.items():
	print("\nMember: "+name, "and is the " +title)
	friend = peoples_friends["Daniel's friend"] + " " + peoples_friends["Aylin"]

		
