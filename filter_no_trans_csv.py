import csv

# Define the input and output file names
input_file = r'C:\Users\romas\Documents\Code\Parsing\01_translation_fi_en.csv'
output_file = r'C:\Users\romas\Documents\Code\Parsing\output.csv'

# Open the input file for reading and the output file for writing
with open(input_file, 'r', newline='',encoding='utf-8-sig') as input_csv, open(output_file, 'w', newline='', encoding='utf-8-sig') as output_csv:
    # Create CSV readers and writers
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)

    # Write the header row to the output CSV
    header = next(reader)
    writer.writerow(header)

    # Loop through the rows and filter based on your condition
    for row in reader:
        translation = row[2]
        if translation != 'no translation':
            writer.writerow(row)

print("Filtered data saved to", output_file)