import re

def main():
    print("Welcome to the email-extractor.\nIt helps you extract an email from a text.Try it!")
    while True:
        text = input("Enter a text to extract an email from: ")
        pattern = r"[\w\.-]+@[\w\.-]+\.[\w]+"
        
        emails = re.findall(pattern, text)
        if len(emails) == 0:
            print("There doesn't seem to appear a valid email address in the input text.")
        else:
            print("\nEmail(s) extracted from the text:")
            for index, email in enumerate(emails, 1):
                print(f"Email {index}: {email} ")
        try_again = input("Would you like to try again? (y/n): ").strip().lower()[0]
        if try_again != "y":
            print("Thank you for using the email-extractor. Good bye!")
            break
        
        
    
if __name__ == "__main__":
    main()
    
