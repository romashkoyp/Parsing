import os
import csv
import xml.etree.ElementTree as ET

# Directory containing your XML files
xml_directory = r'C:\Users\romas\Documents\Code\Parsing\Sources\All Finnish words'

# List to store extracted text
extracted_text = []

# Iterate through XML files in the directory
for filename in os.listdir(xml_directory):
    if filename.endswith('.xml'):
        file_path = os.path.join(xml_directory, filename)
        
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Find all elements with the specified tag and attribute
        search_form_elements = root.findall('.//s')
        
        # Extract and append text from each element to the list
        for element in search_form_elements:
            text = element.text
            if text is not None:
                extracted_text.append(text)

# Sort the list of words alphabetically
extracted_text.sort()

# Create and write to a CSV file with 'utf-8' encoding
with open("finnish_all_words.csv", mode="w", newline='', encoding='utf-8') as csv_file:
    fieldnames = ['word', 'type']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write the data with 'all' as the type for all words
    for text in extracted_text:
        writer.writerow({'word': text, 'type': 'all'})

print("Data saved to finnish_all_words.csv")
