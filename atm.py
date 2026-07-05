
wrong_counts = 0


def withdraw():
    amount = input("Enter the amount to withdraw: ")
    print(f"Withdrawing ${amount}...")


while wrong_counts < 3:
    x = input("Enter your PIN: ")
    if x == "1234":
        print("PIN accepted.")
        withdraw()
        break
    else:
        wrong_counts += 1
        print("Invalid PIN. Please try again.")
else:
    print("Too many failed attempts")