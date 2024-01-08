import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the website and get the response
url = "https://fi.wiktionary.org/wiki/Luokka:Suomen_kielen_verbit"
response = requests.get(url)

# Parse the HTML content of the webpage using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Define a list of Finnish alphabet letters
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"]

# Initialize a dictionary to store verbs for each letter
verbs_by_letter = {}

# Iterate through the letters and extract verbs for each letter
for letter in letters:
    # Find the heading for the current letter
    heading_a = soup.find("h3", string=letter)
    
    if heading_a:
        # Find the list of Finnish verbs under this heading
        verbs = [link.text.strip() for link in heading_a.find_next("ul").find_all("a")]
        
        # Filter out verbs with spaces
        verbs = [verb for verb in verbs if ' ' not in verb]
        
        # Store the verbs in the dictionary
        verbs_by_letter[letter] = verbs

# Print the verbs for each letter, each on a new line
for letter, verbs in verbs_by_letter.items():
    for verb in verbs:
        print(verb)
