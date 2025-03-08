import re

def get_input():
    while True:
        name = input("Enter a name: ")
        try:
            if not name.isalpha():
                raise ValueError("Input valid name.")
            break
        except ValueError as e:
            print(f"Error: {e} Try again.")
    
    while True:
        age = input("Enter age: ")
        try:
            if not age.isnumeric() or int(age) <=0:
                raise ValueError("Input valid age.")
                age = int(age)
            break
        except ValueError as e:
            print(f"Error: {e} Try again.")
        
    while True:
        email = input("Enter email address: ")
        try: 
            if not re.search(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                raise ValueError("Enter a valid email")
            break
        except ValueError as e:
            print(f"Error: {e}. Try again")
        
    return (name.capitalize(), age, email)

def add_guest(guests):
    name, age, email = get_input()
    if name in guests:
        print(f"{name} is already on the list.")
        choice = input("Do you want to update their details? (yes/no):").strip().lower()[0]
        if choice == "y":
            guests[name] = (age, email)
            print(f"{name}'s details updated successfully.")
        else:
            guests[name] = (age, email)
            print(f"{name} is already on the list")
    else:
        guests[name]= (age, email)
        print(f"{name} added successfully.")
    

def remove_guest(guests):
    name = input("Enter the guest's name to be removed: ").capitalize()
    if name in guests.keys():
        del guests[name]
        print(f"{name} removed from the list")
    else:
        print(f"{name} is not on the guest list")

def get_guest_info(guests):
    name = input("Enter the guest's name: ").capitalize()    
    
    if len(guests.keys()) == 0:
        print("The guest list is empty")
    elif name in guests:
        age, email = guests[name]
        print(f"{name} (Age: {age}) is coming to the party! Email: {email}")
    else:
        print(f"{name} is not on the guest list")

def guest_counter(guests):
    guest_count = len(guests.keys())
    print(f"Number of guests: {guest_count}")
    

def main():
    guests = {
        "Alice": (28, "alice@gmail.com"),
        "Bob": (35, "bob@gmail.com"),
        "Charlie": (30, "charlie@gmail.com")
    }

    guests["David"] = (22, "david@gmail.com")
    guests.pop("Bob", "None")   
    
    print("Welcome to the party manager.")
    while True:
        print("""
            What would you like to do?
            1. Add a guest
            2. Remove a guest
            3. Check for a guest
            4. Get number of invited guests
            5. Exit       
              """)
        choice = int(input("Enter your choice: "))
        while True:
            try:
                if choice <1 or choice > 5:
                    raise ValueError("Invalid choice")
                break
            except ValueError as e:
                print("Error: {e}. Try again")
        if choice == 1:
            add_guest(guests)
        elif choice == 2:
            remove_guest(guests)
        elif choice == 3:
            get_guest_info(guests)
        elif choice == 4:
            guest_counter(guests)
        else:
            print("Good Bye!")
            break 
                    
if __name__ == "__main__":
    main()
            
    
            
    