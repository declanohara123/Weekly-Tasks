# Simple BMI Calculator

h = float(input("Enter height in cm: "))
w = float(input("Enter weight in kg: "))

h = (h / 100) ** 2

BMI = (w / h)

BMI = (round (BMI,2))

print("Your BMI is: " , BMI )
