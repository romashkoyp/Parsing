import requests
from bs4 import BeautifulSoup
import csv

# Define the input and output CSV files
input_csv = r'C:\Users\romas\Documents\Code\Parsing\finnish_adjs_i_wiki_20.09.2023.csv'
output_csv = r'C:\Users\romas\Documents\Code\Parsing\finnish_adjs_i_mon_part.csv'

# Create a CSV file for storing the partitiivi forms with the added "Type" column
with open(output_csv, 'w', newline='', encoding='utf-8-sig') as output_file:
    fieldnames = ["word", "type", "mon_part"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

# Function to extract the Partitiivi form from kieli.net
def get_partitiivi_form(word: str) -> str:
    try:
        url = f"https://kieli.net/sana/{word}"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'})

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the <td> elements with title "Partitiivi"
            partitiivi_rows = soup.find_all("td", {"title": "Partitiivi"})

            for partitiivi_row in partitiivi_rows:
                # Check if there is a <td> element after the "Par" one (which contains "-ta")
                next_td = partitiivi_row.find_next("td")
                if next_td and "-ta" in next_td.text:
                    # Extract the value from the following <td><p> element
                    next_next_td = next_td.find_next("td")
                    partitiivi_form = next_next_td.find_next("td").find("p").text
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
        else:
            print(f"No Partitiivi form found for {word}")

print("Partitiivi forms extracted and saved to", output_csv)
