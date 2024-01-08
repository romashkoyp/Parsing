import requests
from bs4 import BeautifulSoup
import csv
import random
import concurrent.futures
import time

# Define the input and output CSV files
input_csv = r'words_without_translation.csv'
output_csv = r'translation_kieli.csv'

# Define the list of user agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/94.0.992.50 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/93.0.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/78.0.4093.214',
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/16.16299",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.0.0 Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/54.0",
]

# Create a CSV file for storing the partitiivi forms with the added "Type" column
with open(output_csv, 'w', newline='', encoding='utf-8-sig') as output_file:
    fieldnames = ["word", "type", "translation"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

# Function to scrape a single page and return the translation
def scrape_page(word):
    word_type = None
    try:
        url = f"https://kieli.net/sana/{word}"
        headers = {'User-Agent': random.choice(user_agents)}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            a_rows = soup.find_all("a", {"href": "#", "ufi": "0"})

            if a_rows:
                first_element_text = a_rows[0].text

                if first_element_text != word:
                    return None

                translation_h2 = soup.find('h2', string='Translations')

                if translation_h2:
                    first_translation_cell = translation_h2.find_next('td')

                    if first_translation_cell:
                        return first_translation_cell.text

    except Exception as e:
        print(f"Error extracting translation for {word}: {e}")

    # Add a random time delay between 0.2 and 0.8 seconds
    random_delay = random.uniform(0.2, 0.8)
    time.sleep(random_delay)

# Define the maximum number of concurrent workers (you can adjust this)
max_workers = 10

# Read the list of Finnish words from the input CSV file
with open(input_csv, 'r', encoding='utf-8-sig') as input_file:
    reader = csv.DictReader(input_file)

    # Create a ThreadPoolExecutor with the specified number of workers
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
        futures = {executor.submit(scrape_page, row['word']): row for row in reader}

        for future in concurrent.futures.as_completed(futures):
            row = futures[future]
            word_type = row['type']
            word_translation = future.result()

            if word_translation:
                with open(output_csv, 'a', newline='', encoding='utf-8-sig') as output_file:
                    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                    writer.writerow({"word": row['word'], "type": word_type, "translation": word_translation})

print("Translation extracted and saved to", output_csv)
