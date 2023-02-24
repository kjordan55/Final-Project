import requests
from bs4 import BeautifulSoup

def get_keywords(url):
    # Send a request to the website and retrieve its HTML content
    response = requests.get(url)
    html_content = response.content

    # Use BeautifulSoup to parse the HTML content and extract the keywords
    soup = BeautifulSoup(html_content, 'html.parser')
    keywords = [meta['content'] for meta in soup.find_all('meta', attrs={'name': 'keywords'})]

    # Strip any extra whitespace from the keywords
    keywords = [keyword.strip() for keyword in keywords]

    return keywords

# get the keywords
url = 'https://www.google.com'
keywords = get_keywords(url)
print(keywords)