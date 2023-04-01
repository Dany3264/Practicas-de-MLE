polling_active = True

while polling_active:
    visit = input("\nWhich place would you like to visit?: ").strip().title()
    print(f"I would like to visit {visit} too!")

    exit = input("\nAnyone else?: ").title()
    if exit == "No":
        polling_active = False