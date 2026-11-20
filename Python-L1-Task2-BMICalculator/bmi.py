# BMI Calculator - OIBSIP Task 2
# Author: Ene Emmanuel

print("--- BMI CALCULATOR ---")

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

print(f"\nYour BMI is: {bmi:.2f}")

# Show category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

print("\nThank you for using BMI Calculator!")
