
def convert_date(date_str, from_cal, to_cal):
    year, month, day = date_str.split("-")
    year = int(year)
 
    if from_cal == to_cal:
        new_year = year
    elif from_cal == "AD" and to_cal == "BS":
        new_year = year + 56
    elif from_cal == "BS" and to_cal == "AD":
        new_year = year - 56
 
    new_date = str(new_year) + "-" + month + "-" + day
    return new_date
 
 
customers = [
    {"name": "Ramesh Thapa",  "date": "1985-06-24", "cal": "AD", "need": "BS"},
    {"name": "Sunita Karki",  "date": "2055-09-10", "cal": "BS", "need": "AD"},
    {"name": "Bikash Rai",    "date": "1998-11-30", "cal": "AD", "need": "BS"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD"},
]
 
print("Date converter")
for c in customers:
    converted = convert_date(c["date"], c["cal"], c["need"])
    print(c["name"] + " | Original: " + c["date"] + " " + c["cal"] +
          " | Converted: " + converted + " " + c["need"])
