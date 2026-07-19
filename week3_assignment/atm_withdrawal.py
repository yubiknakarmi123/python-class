def atm_withdrawal(balance, daily_withdrawn, amount):
    if amount % 500 != 0:
        print("Invalid amount, Must be a multiple of NPR 500")
        return
    if daily_withdrawn + amount > 50000:
        print("Daily withdrawal limit reached")
        return
    if amount > balance:
        print("Insufficient balance")
        return
    balance -= amount
    print("Withdrawal successful")
    print(f"Your current balance after withdrawal: NPR {balance}")
 
print("--- ATM System---")
atm_withdrawal(10000, 20000, 1500) 
print("\n")  
atm_withdrawal(10000, 20000, 1234)
print("\n")
atm_withdrawal(10000, 20000, 60000)   
print("\n")
atm_withdrawal(10000, 49500, 1000)
 