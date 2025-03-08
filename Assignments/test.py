import re
text = input("Enter a text to extract an email from: ")
pattern = r"[\w\.-]+@[\w\.-]+\.[\w]+"
    
email = re.findall(pattern, text)

if email:
    print(f"{email}")
else: 
    print("None")