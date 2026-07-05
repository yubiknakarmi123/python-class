#grade sheet

x = input("marks of the student")

if int(x) >= 90 and int(x)<(100):
    print("Distinction")
elif int(x) >= 75 and int(x)<90:
    print("first division")
elif int(x)>=60 and int(x)<90:
    print("second divisiohn")
elif int(x)>=35 and int(x) <60:
    print("third division")
else:
    print("fail")