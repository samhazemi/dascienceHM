import os
import csv
import operator 
file_numbers=['1','2']
max_revenue=[]
min_revenue=[]
for filenum in file_numbers:
    pybankcsv= os.path.join( 'budget_data_' + filenum +'.csv')
    with open(pybankcsv,'r') as csvfile:
                csvreader=csv.reader(csvfile,delimiter=",")
                next(csvreader)
                revenue_holder=[]
                Total_revenue=0
                Total_months=0
                row_holder=next(csvreader)
                for row in csvreader:
                    revenue=row_holder[1]
                    month_holder=row[0]
                    if row[1] > revenue:
                        revenue=row[1]
                        row_holder=row
                        max_revenue=row
                        print(row_holder)
                    row_holder= (month_holder,revenue)
                    revenue_holder.append(row_holder)
                    Total_revenue=Total_revenue+int(revenue)
                    Total_months += 1
#                    max_row=max(csv.reader(csvreader),key=operator.itemgetter(1))
#                    min_row=min(csv.reader(csvreader),key=operator.itemgetter(1))
print("Total Months:", str(Total_months) )
print("Total Revenue:" , str(Total_revenue) )
print("Greatest Increase in Revenue: ", max_revenue)
print("Greatest Decrease in Revenue: ", min_row)
print("row_holder: ", row_holder)
