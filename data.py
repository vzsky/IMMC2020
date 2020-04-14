import csv, json

csvFile = "/Users/mb99n/Desktop/IMMC/StoreData.csv"

cnt = 0

data = []
with open (csvFile, 'r+') as file : 
    csvReader = csv.DictReader(file)
    for row in csvReader :
        del row['']
        row['Rating'] = float(row['Rating'])
        row['Quantity'] = int(row['Quantity'])
        row['Price'] = float(row['Price'].replace('$', '').replace(',', ''))
        row['Regular Price'] = float(row['Regular Price'].replace('$', '').replace(',', ''))
        row['Discount'] = row['Regular Price'] - row['Price']

        data.append(row)

# Department
# Category
# Product Type
# Brand
# Product
# Regular Price
# Price
# Quantity
# Rating