# Momo shop, Yubik nakarmi

cost_price = float(input("Enter cost price per plate (Rs): "))
selling_price = float(input("Enter selling price per plate (Rs): "))
plates_sold = int(input("Enter number of plates sold today: "))

total_revenue = selling_price * plates_sold
total_cost = cost_price * plates_sold
total_profit = total_revenue - total_cost
profit_margin = (total_profit / total_revenue) * 100

print(f"\nTotal revenue: Rs {total_revenue:}")
print(f"Total cost: Rs {total_cost:}")
print(f"Total profit: Rs {total_profit:}")
print(f"Profit margin: {profit_margin:}%")