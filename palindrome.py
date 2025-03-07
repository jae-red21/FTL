def is_palindrome_for(input_str: str) -> bool:
    input_str = input_str.lower()
    cleaned_input = ''.join(char for char in input_str if char.isalnum())
            
    for i in range(len(cleaned_input)//2):
        if cleaned_input[i] != cleaned_input[len(cleaned_input) -i -1]:
            print("Checked with for loop: Result: The input is not Palindrome")
            break
    else: 
        print("Checked with for loop: Result: The input is a Palindrome")

def is_palindrome_while(input_string: str) -> bool:
    input_string = input_string.lower()
    cleaned_input = ''.join(char for char in input_string if char.isalnum())
    
    i = 0
    while(i < len(cleaned_input)//2):
        if cleaned_input[i] != cleaned_input[len(cleaned_input) -i -1]:
            print("Checked with while loop: Result:  The input is not Palindrome")
            break
        else:
            print("Checked with while loop: Result:  The input is Palindrome")
            break
        i += 1
        
        
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
        
        is_palindrome_for(word)
        is_palindrome_while(word)
        response = input("Wanna try another word? (y/n)").strip().lower()[0]
        if response != "y":
            print("Good Bye!")
            break
        
    
        
        
if __name__=="__main__":
    main()
            
            
        