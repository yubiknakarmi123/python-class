monthly_salary = float(input("Enter monthly basic salary: "))
deduction_percent = 10 

bonus = monthly_salary
deduction = bonus * (deduction_percent / 100)
final_bonus = bonus - deduction

print(f"Dashain bonus: Rs {bonus:.2f}")
print(f"Deduction: Rs {deduction:.2f}")
print(f"Final take-home bonus: Rs {final_bonus:.2f}")