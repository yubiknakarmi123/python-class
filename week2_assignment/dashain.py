# Dashain Bonus Calculator, Yubik nakarmi


monthly_salary = float(input("Enter employee's monthly basic salary"))

deduction_percent = 1  

dashain_bonus = monthly_salary * 1  # one month's salary
deduction = dashain_bonus * (deduction_percent / 100)
take_home_bonus = dashain_bonus - deduction

print(f"Gross Dashain bonus: Rs {dashain_bonus}")
print(f"Deduction ({deduction_percent}%): Rs {deduction}")
print(f"Final take-home bonus: Rs {take_home_bonus}")