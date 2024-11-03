# Taking user inputs for weight and height
weight=float(input("Enter your weight in kilograms: "))
height=float(input("Enter your height in meters: "))

# calculating bmi
bmi= weight / (height ** 2)

# Display the calculated BMI
print(f"Your BMI is: {bmi: .2f}")

# Conditional checks based on the calculated BMI
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")

