import requests
from bs4 import BeautifulSoup
import csv
import time
import random

# Define the input and output CSV files
input_csv = r'C:\Users\romas\Documents\Code\Parsing\finnish_two-syllable_a_words.csv'
output_csv = r'C:\Users\romas\Documents\Code\Parsing\finnish_two-syllable_a_words_part.csv'

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
    fieldnames = ["word", "type", "mon_part"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

# Function to extract the Partitiivi form from kieli.net
def get_partitiivi_form(word: str) -> str:
    try:
        url = f"https://kieli.net/sana/{word}"
        # Choose a random user agent from the list
        headers = {'User-Agent': random.choice(user_agents)}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find nominatiivi form to compare with the original word
            nominatiivi_rows = soup.find_all("tr", {"cid": "0"})

            for nominatiivi_row in nominatiivi_rows:
                # Check if there is a <td> element with text "-" (Nom)
                next_td = nominatiivi_row.find("td", string="-")
                if next_td:
                    # Find the <td> element in the next position within the current row
                    next_td = nominatiivi_row.find_all("td")[-2]
                    # Extract the text from the <p> element within the last <td>
                    nominatiivi_form = next_td.find("p").text
                    if nominatiivi_form != word:
                        print(f"'{word}' does not match the nominatiivi form '{nominatiivi_form}'. Skipping.")
                        return None
                    break

            # If the nominatiivi form matches, proceed to find the Partitiivi form
            # Find all the <tr> elements with cid "1"
            partitiivi_rows = soup.find_all("tr", {"cid": "1"})

            for partitiivi_row in partitiivi_rows:
                # Check if there is a <td> element with text "-ta" (Par)
                next_td = partitiivi_row.find("td", string="-ta")
                if next_td:
                    # Find the <td> element in the last position within the current row
                    last_td = partitiivi_row.find_all("td")[-1]
                    # Extract the text from the <p> element within the last <td>
                    partitiivi_form = last_td.find("p").text
                    return partitiivi_form

    except Exception as e:
        print(f"Error extracting Partitiivi form for {word}: {e}")
        return None

# Read the list of Finnish adjectives from the input CSV file
with open(input_csv, 'r', encoding='utf-8-sig') as input_file:
    reader = csv.DictReader(input_file)

    for row in reader:
        word = row['word']
        adjective_type = row['type']
        partitiivi_form = get_partitiivi_form(word)

        if partitiivi_form:
            with open(output_csv, 'a', newline='', encoding='utf-8-sig') as output_file:
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writerow({"word": word, "type": adjective_type, "mon_part": partitiivi_form})

        # Sleep for a random time between 0.1 and 0.2 seconds
        sleep_time = random.uniform(0.1, 0.2)
        time.sleep(sleep_time)

print("Partitiivi forms extracted and saved to", output_csv)
