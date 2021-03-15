# Create an Excel file with 20 data sets (rows) where Number and Price are two columns.
# Write a python program to read that Excel file and then multiply these two Coulmns Number and Price.

# For the above Excel file, use the groupby module for certain criteria based on your choice.

# Draw a linear regression model for the created Excel file considering
# the x-axis values are Number and Y-axis value are Price.

import pandas as pd
import xlsxwriter as xc
import random
import matplotlib.pyplot as plt
from scipy.stats import linregress

filename = r"pricelist.xlsx"


workbook = xc.Workbook(filename)
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, "Amount")
worksheet.write(0, 1, "Price")

for i in range(1, 21):
    worksheet.write(i, 0, random.randint(1, 15))
    worksheet.write(i, 1, random.randint(1, 100))
workbook.close()


data = pd.read_excel(filename)
data['New_Clmn'] = data['Amount']*data['Price']
dataToInsert = data.New_Clmn.to_numpy()

print(dataToInsert)

group = data.groupby('Amount')
print(group.get_group(10))

x = data.Amount
y = data.Price
stats = linregress(x, y)
m = stats.slope
b = stats.intercept
plt.figure(figsize=(10, 10))
plt.scatter(x, y, marker='+')
plt.plot(x, m*x + b, color="red", linewidth=3)
plt.xlabel("Amount", fontsize=20)
plt.ylabel("Price", fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.savefig("python-linear-reg-custom.png")
