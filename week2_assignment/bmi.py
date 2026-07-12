# BMI calculator, Yubik Nakarmi

weight_kg = float(input("Enter weight (kg): "))
height_cm = float(input("Enter height (cm): "))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

print(f"\nHeight in meters: {height_m} m")
print(f"BMI: {bmi}")