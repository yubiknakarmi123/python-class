import pandas as pd
class_data = {f"student_{i}": {"marks": int(input(f"Enter marks for student_{i}: ")), "grade": ""} for i in range(1, 20)}


for student,marks in class_data.items():
    x = marks["marks"]

    if int(x)>100:
        marks["grade"]="invalid grade"
    if int(x) >= 90 and int(x)<(100):
        marks["grade"]="distinction"
        
    elif int(x) >= 75 and int(x)<90:
        marks["grade"]="first division"

    elif int(x)>=60 and int(x)<90:
        marks["grade"]="second division"
    elif int(x)>=35 and int(x) <60:
        marks["grade"]="third division"
    else:
        marks["grade"]="fail"
        
    marks["marks"]
df = pd.DataFrame(class_data)
df.to_csv("class_report.csv")
print(f"saved at class_report.csv")