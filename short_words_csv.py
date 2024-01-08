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

# Define your pattern samples and their corresponding lengths
pattern_samples = ['cVVccVc', 'cVVccV', 'cVVcV', 'VVcV', 'VVccV', 'VVccVc', 'VVcVc']
pattern_lengths = [7, 6, 5, 4, 5, 6, 5]  # Lengths corresponding to each pattern

# Function to check if a word matches a pattern
def matches_pattern(word, pattern):
    return all(c1 == c2 or (c1 == 'c' and c2 in 'bcdfghjklmnpqrstvwxz') or (c1 == 'V' and c2 in 'aeiouyöäå') for c1, c2 in zip(pattern, word))

matching_words = []

# Find words that match the pattern samples
for pattern, length in zip(pattern_samples, pattern_lengths):
    filtered_words = [word for word in combined_data if len(word) == length]
    matching_words.extend([word for word in filtered_words if matches_pattern(word, pattern)])

# Save the filtered data to a new CSV file
with open('filtered_data.csv', 'w', encoding='utf-8-sig', newline='') as filtered_file:
    writer = csv.writer(filtered_file)
    writer.writerows([[word] for word in matching_words])  # Writing each word as a list to match CSV format



    