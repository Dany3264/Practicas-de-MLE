#6-1. Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each
#piece of information stored in your dictionary.

person = {"first_name": "Aylin",
    "last_name": "Solis",
    "age": "21 years old",
    "city": "whitby, ontario"}

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

people_numbers = {"Aylin": "10", "Daniel": "15", "Liam": "20", "Elaine": "25", "Adeleide": "30"}

aylin_number = people_numbers["Aylin"].title()
daniel_number = people_numbers["Daniel"].title()
elaine_number = people_numbers["Elaine"].title()
liam_number = people_numbers["Liam"].title()
adeleide_number = people_numbers["Adeleide"].title()

print(f"\t\nAylin's favourite number is: \n#{aylin_number}")
print(f"\t\nDaniel's favourite number is: \n#{daniel_number}")
print(f"\t\nElaine's favourite number is: \n#{elaine_number}")
print(f"\t\nLiam's favourite number is: \n#{liam_number}")
print(f"\t\nAdeleide's favourite number is: \n#{adeleide_number}")


for name, number in people_numbers.items():
	print(f"{name}'s favourite number is:\n{number}")
    