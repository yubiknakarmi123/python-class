passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]
special_chars = "!@#$%^&*"
 
print("--- Password Strength Checker ---")
for pw in passwords:
    missing = []
    if len(pw) < 8:
        missing.append("at least 8 characters")
    if not any(c.isupper() for c in pw):
        missing.append("an uppercase letter")
    if not any(c.islower() for c in pw):
        missing.append("a lowercase letter")
    if not any(c.isdigit() for c in pw):
        missing.append("a digit")
    if not any(c in special_chars for c in pw):
        missing.append("a special character")
 
    if missing:
        print(f"{pw}: Weak - missing {', '.join(missing)}")
    else:
        print(f"{pw}: Strong")