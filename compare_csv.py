import csv

# Read the words from the first CSV file (bigger one)
with open(r'words_for_translation.csv', 'r', encoding='utf-8-sig') as file1:
    reader1 = csv.reader(file1)
    words1 = [word[0] for word in reader1]

# Read the words from the second CSV file (smaller one)
with open(r'translation_babla.csv', 'r', encoding='utf-8-sig') as file2:
    reader2 = csv.reader(file2)
    words2 = [word[0] for word in reader2]

# Find non-matching words
original_words = [word for word in words1 if word not in words2]

# Write the non-matching words to a new CSV file with the 'type' column
with open('words_no_translation.csv', 'w', newline='', encoding='utf-8-sig') as output_file:
    writer = csv.writer(output_file)
    for word in original_words:
        writer.writerow([word, 'wiki', 'no translation'])

print("Non-matching words have been written")

