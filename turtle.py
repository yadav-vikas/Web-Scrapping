import requests
from bs4 import BeautifulSoup
import pandas as pd

prefix = "https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/"
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them"
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0].get_text()
  
  stats = turtle.find("ul")
  stats_text = stats.get_text("|")
  turtle_data[turtle_name] = stats_text.split("|")
#creating dataframe from the dictionary
turtle_df =pd.DataFrame.from_dict(turtle_data)
print(turtle_df.head())
