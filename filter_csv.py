import csv
import re

# Specify the input and output CSV file names
input_file = r'C:\Users\romas\Documents\Code\Parsing\Data\finnish_two-syllable_a_words_part.csv'
output_file = r'C:\Users\romas\Documents\Code\Parsing\Data\finnish_two-syllable_a_words_part_hauska_koira.csv'

# Regular expression to match words ending with different endings
pattern_hauska = re.compile(r'oja$|ojä$')
pattern_koira= re.compile(r'ita$|itä$|ia$|iä$')

# Create a list to store the rows that meet the criteria
filtered_data = []

# Open the input CSV file for reading with the specified encoding (try different encodings if needed)
with open(input_file, 'r', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    # Append the header row to the filtered data
    header = next(reader)
    header.insert(2, 'type_2')  # Add 'age' between columns [1] and [2]
    filtered_data.append(header)

    # Iterate through the rows
    for row in reader:
        if len(row) >= 3:  # Make sure there are at least 3 columns in a row
            sana = row[2]
            # Check if the word ends with
            if pattern_hauska.search(sana):
                row.insert(2, 'hauska')
                filtered_data.append(row)
            # Check if the word ends with 'eita' or 'eitä' or 'eja' or 'ejä'
            elif pattern_koira.search(sana):
                row.insert(2, 'koira')
                filtered_data.append(row)

# Write the filtered data to the output CSV file with UTF-8 encoding
with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(filtered_data)

print(f"Filtered CSV file '{output_file}' created successfully.")
