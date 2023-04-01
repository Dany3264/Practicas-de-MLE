def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title().strip()

while True:
    print("Name?")
    print("Please press 'q' at any time to exit.")
    f_name = input("First name?: ").lower()
    if f_name == "q":
        break

    l_name = input("Last name?: ").lower()
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello {formatted_name}, nice to meet you!")