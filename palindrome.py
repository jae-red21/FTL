def check_palindrome(input_str: str) -> bool:
    input_str = input_str.lower()
    cleaned_input = ''.join(char for char in input_str if char.isalnum())
            
    for i in range(len(cleaned_input)//2):
        if cleaned_input[i] != cleaned_input[len(cleaned_input) -i -1]:
            print("Not Palindrome")
            break
    else: 
        print("Palindrome!")

def main():
    print("Welcome to the Palindrome checker.");
    while True:
        while True:
            word = input("Enter a word (or a sentence): ")
            try:
                if len(word) <=0:
                    raise ValueError("You didn't enter anything. Try again")
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        check_palindrome(word)
        response = input("Wanna try another word? (y/n)").strip().lower()[0]
        if response != "y":
            print("Good Bye!")
            break
        
        
if __name__=="__main__":
    main()
            
            
        