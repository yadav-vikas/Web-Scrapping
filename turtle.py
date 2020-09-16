import requests
from bs4 import BeautifulSoup

prefix = "https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/"
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')
#adding URL and its contents
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
#finding and storing all the anchor elements
turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
  links.append(prefix+a["href"])
#storing all the links in links(list) to get data    
#Define turtle_data: for storing the data for each name and its values
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  #selecting the name of that turtle from the "name" class
  turtle_name = turtle.select(".name")[0]
  #adding key and values to dictionary turtle_data
  turtle_data[turtle_name.get_text()] = [turtle.find("li").get_text("|")]

print(turtle_data)
print(soup.find_all("li"))
