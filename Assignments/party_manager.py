guest_list = []
def add_guest():
    while True:
        try:
            name = input("Enter guest's name: ")
            if len(name) < 1 or name.isdigit():
                raise ValueError("Enter a valid name")
            break
        except ValueError as e:
            print(f"Error: {e}")

    name = name[0].upper() + name[1:]
    if name in guest_list:
        print(f"\nGuest {name} already exists!")
    guest_list.append(name)
    print(f"\nGuest {name} added!")


def remove_guest():
    while True:
        try:
            name = input("Enter guest's name: ")
            if len(name) < 1 or name.isdigit():
                raise ValueError("Enter a valid name")
            break
        except ValueError as e:
            print(f"Error: {e}")
    name = name[0].upper() + name[1:]
    if not name in guest_list:
        print("\nGuest not found")
    elif len(guest_list) == 0:
        print("No guests found")
    else:
        guest_list.remove(name)
        print(f"\nGuest {name} removed!")

def show_guests():
    if len(guest_list) == 0:
        print("\nNo guests found")
    else:
        guests = [name for name in guest_list]
        print("Guests:")
        print(*guests, sep=", ")


def check_guest():
    while True:
        try:
            name = input("Enter guest's name: ")
            if len(name) < 1 or name.isdigit():
                raise ValueError("Enter a valid name")
            break
        except ValueError as e:
            print(f"Error: {e}")
    name = name[0].upper() + name[1:]
    if not name in guest_list:
        print(f"\n{name} not found in the party list")
    else:
        print(f"\nGuest: {name} is in the party list")

def main():
    print("Welcome to the party organizer.")
    while True:
        print("""
What would you like to do?
1. Add a guest to the party
2. Remove a guest from the party
3. Check if a guest is in the party
4. See everyone in the party
5. Exit
                            """)
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice < 1 or choice > 5:
                    raise ValueError("Invalid choice")
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

        if choice == 1:
            add_guest()
        elif choice == 2:
            remove_guest()
        elif choice == 3:
            check_guest()
        elif choice == 4:
            show_guests()
        elif choice == 5:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()