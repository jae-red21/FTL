def bmi_calculator(height:float, weight: float) -> float:
    return weight / (height ** 2)

def main():
    print("Welcome to the BMI Calculator!")
    while True:
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))
        bmi: float = bmi_calculator(weight, height)
        print("Your BMI is: ", bmi)
        response = input("Would you like to try again? (y/n): ").strip().lower()[0]
        if response != "y":
            print("Thank you for using BMI Calculator!")
            break

if __name__ == "__main__":
    main()