import csv

# Read the words and their details from the first CSV file
with open(r'filtered_data.csv', 'r', encoding='utf-8-sig') as file1:
    reader1 = csv.reader(file1)
    data1 = [row for row in reader1]

# Read the words and their details from the second CSV file
with open(r'filtered_data_2.csv', 'r', encoding='utf-8-sig') as file2:
    reader2 = csv.reader(file2)
    data2 = [row for row in reader2]

# Read the words and their details from the first CSV file
with open(r'filtered_data_3.csv', 'r', encoding='utf-8-sig') as file3:
    reader3 = csv.reader(file3)
    data3 = [row for row in reader3]

# Read the words and their details from the second CSV file
with open(r'Data\05_one_two_syl.csv', 'r', encoding='utf-8-sig') as file4:
    reader4 = csv.reader(file4)
    data4 = [row for row in reader4]

# Combine the data from both CSV files
combined_data = data1 + data2 + data3 + data4

# Save the combined data to a new CSV file
with open('combined_data.csv', 'w', encoding='utf-8-sig', newline='') as combined_file:
    writer = csv.writer(combined_file)
    writer.writerows(combined_data)
