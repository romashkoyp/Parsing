import pandas as pd

# Load the original CSV file
df = pd.read_csv('translation_kieli.csv')

# Filter the DataFrame based on the specified conditions
filtered_df = df[(df['word'] != df['translation']) & (df['translation'].str.len() >= 3)]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('merged_output_kieli_minus_short_same.csv', index=False)