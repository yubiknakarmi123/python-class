def build_profile(name, **details):
    print(f"Name: {name}")
    for key, value in details.items():
        print(f"{key}: {value}")
 
build_profile("Sita", branch="Computer Science", portfolio="sita.dev")
print()
build_profile("Ram", branch="Business Studies")