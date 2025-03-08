calculate_bmi = lambda height, weight: weight/(height*height)

def main():
    print("Welcome to the BMI Calculator!")
    while True:
        while True:
            try:
                weight = float(input("Enter weight in kilograms: "))
                
                if weight <= 0.0:
                    raise ValueError("Weight must be greater than zero.")
                break
            except ValueError as e:
                print(f"Error: {e} Please Try again")
        
        while True:
            try:
                height = float(input("Enter height in meters: "))
                
                if height <= 0.0:
                    raise ValueError("Height must greater than zero.")
                break
            except ValueError as e:
                print(f"Invalid input: {e} Please try again")
                    
            
        bmi: float = calculate_bmi(height, weight)
        print("Your BMI is: ", bmi)
        
        if bmi < 18.5:
            print("Your are underweight.")
        elif bmi < 25:
            print("Your are normal weight.")
        elif bmi < 30:
            print("Your are overweight.")
        else:
            print("Your are Obese.")
        response = input("Would you like to try again? (y/n): ").strip().lower()[0]
        if response != "y":
            print("Thank you for using BMI Calculator!")
            break

if __name__ == "__main__":
    main()