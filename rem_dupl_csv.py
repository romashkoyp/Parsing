import pandas as pd

# Load the original CSV file
df = pd.read_csv(r'C:\Users\romas\Documents\Code\Parsing\combined_data.csv')

# Remove duplicates based on the 'word' column
df = df.drop_duplicates(subset='word', keep='first')

# Sort the DataFrame by the 'word' column
df = df.sort_values(by='word')

# Save the new CSV file without duplicates and sorted by 'word'
df.to_csv('output_data.csv', index=False)