from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')
webpage = webpage_response.content
soup = BeautifulSoup(webpage,"html.parser")
print(soup)
ratings = []
print("---------------------")
rating_list = soup.select(".Rating")
print(rating_list)
for i in range(1,len(rating_list)):
  ratings.append(float(rating_list[i].get_text()))
print("===============================")
print(ratings)
plt.hist(ratings)
plt.show()

companies = []
print("---------------------")
company_list = soup.select(".Company")
print(company_list)
for i in range(1,len(company_list)):
  companies.append(company_list[i].get_text())
print("===============================")
print(companies)

df = pd.DataFrame()
df['ratings']=ratings
df['companies'] = companies
print(df.head())

total_ratings = df.groupby('companies').ratings.sum().reset_index()
print(total_ratings)

largest_10 = total_ratings.nlargest(10,'ratings')
print(largest_10)
