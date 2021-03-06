import csv
import os
total_months= 0
total_revenue = 0
prev_revenue = 0
revenue_change = 0
greatest_increase= ["",0]
greatest_decrease = ["", 999999999999]
revenue_changes = []
csvreader = csv.DictReader(open("raw_data/budget_data_1.csv"))
for row in csvreader:    
                total_months= total_months + 1
                total_revenue=total_revenue + int(row["Revenue"])
#                print(row)
                revenue_change=int(row["Revenue"]) - prev_revenue
                prev_revenue = int(row["Revenue"])
                if (revenue_change > greatest_increase[1]):
                    greatest_increase[1] = revenue_change
                    greatest_increase[0]=row["Date"]
                if (revenue_change < greatest_decrease[1]):
                    greatest_decrease[1] = revenue_change
                    greatest_decrease[0]=row["Date"]
revenue_changes.append(int(row["Revenue"]))
print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(total_months))
print("Totat Revenue: " +"$" + str(total_revenue))
print("Average Change: "+ "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
print("Greatest Increase: " + str(greatest_increase[0] + " ($" + str(greatest_increase[1]) + ")"))
print("Greatest Decrease: " + str(greatest_decrease[0] + " ($" + str(greatest_decrease[1]) + ")"))
