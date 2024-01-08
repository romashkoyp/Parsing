import csv

# Specify the input text file and output CSV file
input_file = r'C:\Users\romas\Documents\Code\Parsing\Sources\suomen-sanomalehtikielen-taajuussanasto-B9996-2.txt'
output_file = r'C:\Users\romas\Documents\Code\Parsing\suomen-sanomalehtikielen-taajuussanasto-B9996.csv'

# Define the desired order of columns
desired_columns = ['Number', 'Abs', 'Rel', 'Sana', 'Typpi']

# Read the data from the input text file
with open(input_file, 'r', encoding='utf-8') as text_file:
    for line in text_file:
        # Split the line using spaces as a delimiter
        parts = line.strip().split()

        # Ensure that the line has the correct number of columns
        if len(parts) == len(desired_columns):
            # Write the data to the output CSV file
            with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(parts)

print(f"CSV file '{output_file}' created successfully.")
