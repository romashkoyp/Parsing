import requests
from bs4 import BeautifulSoup
import csv
import time
import random

# Define a list of user-agents to emulate different browsers and devices
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/16.16299",
    # Add more user-agents as needed
]

# Initialize a list to store all Finnish nouns
all_nouns = []

# Start with the initial page URL
base_url = "https://fi.wiktionary.org/wiki/Luokka:Suomen_kielen_substantiivit"

# Initialize a counter for the number of pages parsed
page_count = 0

while True:  # Remove the page limitation
    # Pick a random user-agent from the list
    user_agent = random.choice(user_agents)

    # Define headers with the selected user-agent
    headers = {'User-Agent': user_agent}

    # Add a random delay to simulate human behavior
    time.sleep(random.uniform(2, 5))  # Adjust the range as needed

    # Send an HTTP request to the current page with the selected user-agent
    response = requests.get(base_url, headers=headers)

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
        # Find the list of Finnish nouns under this heading
        nouns = [link.text.strip() for link in heading.find_next("ul").find_all("a")]

        # Filter out nouns with spaces
        nouns = [noun for noun in nouns if ' ' not in noun]

        # Add the nouns from this section to the list
        all_nouns.extend(nouns)

    # Get the URL of the next page
    base_url = "https://fi.wiktionary.org" + next_page_link["href"]

    # Increment the page count
    page_count += 1

# Sort the list of nouns alphabetically
all_nouns.sort()

# Create and write to a CSV file with 'utf-8' encoding
with open("finnish_nouns.csv", mode="w", newline='', encoding='utf-8') as csv_file:
    fieldnames = ['word', 'type']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write the data with 'substantiivi' as the type for all words
    for noun in all_nouns:
        writer.writerow({'word': noun, 'type': 'substantiivi'})

print("Data saved to finnish_nouns.csv")
