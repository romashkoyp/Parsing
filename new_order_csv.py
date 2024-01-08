import csv

# Specify the input and output CSV file names
input_file = r'C:\Users\romas\Documents\Code\Parsing\Data\suomen-sanomalehtikielen-taajuussanasto-B9996.csv'
output_file = r'C:\Users\romas\Documents\Code\Parsing\Data\suomen-sanomalehtikielen-taajuussanasto-B9996_2.csv'

# Read the data from the input CSV file
data = []
with open(input_file, 'r', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Define the new order of column names
new_column_order = ['word', 'type', 'number', 'abs', 'rel']

# Write the data to the output CSV file with the new column order
with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=new_column_order)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"New CSV file '{output_file}' with reordered columns created successfully.")
