import requests
from bs4 import BeautifulSoup
import csv

# Initialize a list to store all Finnish verbs
all_verbs = []

# Start with the initial page URL
base_url = "https://fi.wiktionary.org/wiki/Luokka:Suomen_kielen_verbit"

# Initialize a counter for the number of pages parsed
page_count = 0

# Set the maximum page count for testing
max_page_count = 3

while page_count < max_page_count:
    # Send an HTTP request to the current page
    response = requests.get(base_url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page: {base_url}")
        break

    # Parse the HTML content of the webpage using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the "seuraava sivu" link tags
    next_page_links = soup.find_all("a", string="seuraava sivu")

    # Check if there are any "seuraava sivu" links
    if not next_page_links:
        print("No more 'seuraava sivu' links found.")
        break

    # Find the next page link
    next_page_link = next_page_links[-1]  # Take the last one, which is the one you want

    # Find the section between "seuraava sivu" links
    section_between_links = next_page_link.find_previous("a", string="seuraava sivu").find_next("a", string="seuraava sivu")

    # Find all headings for the current letters (e.g., "A", "B", etc.) within this section
    headings = section_between_links.find_all_previous("h3")

    for heading in headings:
        # Find the list of Finnish verbs under this heading
        verbs = [link.text.strip() for link in heading.find_next("ul").find_all("a")]

        # Filter out verbs with spaces
        verbs = [verb for verb in verbs if ' ' not in verb]

        # Add the verbs from this section to the list
        all_verbs.extend(verbs)

    # Get the URL of the next page
    base_url = "https://fi.wiktionary.org" + next_page_link["href"]

    # Increment the page count
    page_count += 1

# Sort the list of verbs alphabetically
all_verbs.sort()

# Create and write to a CSV file with 'utf-8' encoding
with open("finnish_verbs.csv", mode="w", newline='', encoding='utf-8') as csv_file:
    fieldnames = ['word', 'type']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write the data with 'verbi' as the type for all words
    for verb in all_verbs:
        writer.writerow({'word': verb, 'type': 'verbi'})

print("Data saved to finnish_verbs.csv")
