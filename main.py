"""
In order to scrape a website, go to the inspect element and the pen marker to actually select
the item that you want to inspect. Then determine how to get to the value you want in the tag that
you want using beautiful soup.
"""
from bs4 import BeautifulSoup
import requests
from datetime import datetime

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
date = "2000-08-12"
# datetime.strftime("%Y-%m-%d")     # format datetime to YYYY-MM-DD

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
print(song_names_spans)

# get text, then strip all the spaces
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

