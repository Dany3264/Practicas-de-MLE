#3-4 pag 42

guests = ["Daniel", "Aylin", "Adeleide"]

print(f"\nHi {guests[0]}, I´m organizing a nice dinner tonight, would you like to join us?")
print(f"\nHello {guests[1]}, we are throwing a great dinner tomorrow, would you like to come?")
print(f"\nGood morning {guests[2]}, would you like to have dinner tonight with us?")

print(f"\n{guests[-1]}")

guests[-1] = "Elaine"
print(guests)


print(f"\nHello {guests[0]}, Adeleide will not be able to come.")

print(f"\nHi again, {guests[1]}!, im sorry to inform you that Adeleideis not coming tomorrow.")

print(f"\nHow's it going {guests[-1]}, we hace an open seat for our dinnr party tonight, would you like to join us?")

print("Good news everyone, we have more space for dinner!")

guests.insert(0, "Isaac")
guests.insert(2, "Adeleide")
guests.append("Liam")
print(guests)

#guests = ["Daniel", "Aylin", "Adeleide"]


print(f"\nHello {guests[1]}, Adeleide will be able to come.")

print(f"\nHi again, {guests[3]}!, I wanted to inform you that Adeleide is coming tomorrow.")

print(f"\nHow's it going {guests[-2]}, we hace an open seat for our dinnr party tonight, would you like to join us?")

print(f"\nHi {guests[0]}, wanna come to dinner tonight?")

print(f"\nHello {guests[2]}, We are happy to hear that you will be able to come!")

print(f"\nThe whole family is going to be here {guests[-1]}, we would really enjoy you companion tonight")

print("I'm sorry, i can only invite two of you to dinner")

uninvited_guest1 = guests.pop()
uninvited_guest2 = guests.pop(0)
uninvited_guest3 = guests.pop(1)

uninvited_guests = [uninvited_guest3, uninvited_guest2, uninvited_guest1]
print(f"We are very sorry {uninvited_guests}, we cannot invite you to dinner")

print(f"We can still invite you {guests}")
print(sorted(guests))
print(len(guests))
guests.reverse()
print(guests)

print(guests.sort())