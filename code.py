import requests
from bs4 import BeautifulSoup

# Step 1: Make a request to the website
url = 'https://www.bostonglobe.com'  # Replace with the URL you want to scrape
response = requests.get(url)


# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find the <span> tag by its id
span_content = soup.find('span', id='headline-f0fpkbe5wu3y2fh')

# Step 4: Extract the text (or do something with the tag)
if span_content:
    print(span_content.text)
else:
    print("Tag not found")
