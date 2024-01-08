import csv

# Read the words and their details from the first CSV file
with open(r'Data\01_translation_fi_en.csv', 'r', encoding='utf-8-sig') as file1:
    reader1 = csv.reader(file1)
    data1 = [row[0] for row in reader1]  # Assuming the words are in the first column

# Read the words and their details from the second CSV file
with open(r'Data\noun_adj_verb.csv', 'r', encoding='utf-8-sig') as file2:
    reader2 = csv.reader(file2)
    data2 = [row[0] for row in reader2]  # Assuming the words are in the first column

# Combine the data from all CSV files
combined_data = data1 + data2

matching_words = []

# Function to count vowels in a word
def count_vowels(word):
    return sum(1 for c in word if c in 'aeiouyöäå')

# Find words with exactly two vowels and add them to matching_words
for word in combined_data:
    if count_vowels(word) <= 2:
        matching_words.append(word)

# Save the filtered data to a new CSV file
with open('filtered_data_3.csv', 'w', encoding='utf-8-sig', newline='') as filtered_file:
    writer = csv.writer(filtered_file)
    writer.writerows([[word] for word in matching_words])  # Writing each word as a list to match CSV format