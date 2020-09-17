from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading the URL from requests
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')
webpage = webpage_response.content
soup = BeautifulSoup(webpage,"html.parser")
#print(soup)

#creating list for each columns for storing each values from url
#Rating
Rating = []
rating_list = soup.select(".Rating")
#print(rating_list)
for i in range(1,len(rating_list)):
  Rating.append(float(rating_list[i].get_text()))
#print(Rating)
plt.hist(Rating)
plt.show()

#Company
Company = []
company_list = soup.select(".Company")
#print(company_list)
for i in range(1,len(company_list)):
  Company.append(company_list[i].get_text())
#print(Company)

#Origin
Origin = []
origin_list = soup.select(".Origin")
#print(origin_list)
for i in range(1,len(origin_list)):
  Origin.append(origin_list[i].get_text())
#print(Origin)

#REF
REF = []
REF_list = soup.select(".REF")
#print(REF_list)
for i in range(1,len(REF_list)):
  REF.append(float(REF_list[i].get_text()))
#print(REF)

#ReviewDate
ReviewDate = []
ReviewDate_list = soup.select(".ReviewDate")
#print(ReviewDate_list)
for i in range(1,len(ReviewDate_list)):
  ReviewDate.append(ReviewDate_list[i].get_text())
#print(ReviewDate)

#CocoaPercent
CocoaPercent = []
CocoaPercent_list = soup.select(".CocoaPercent")
#print(CocoaPercent_list)
for i in range(1,len(CocoaPercent_list)):
  CocoaPercent.append(CocoaPercent_list[i].get_text())
#print(CocoaPercent)

#CompanyLocation
CompanyLocation = []
CompanyLocation_list = soup.select(".CompanyLocation")
#print(CompanyLocation_list)
for i in range(1,len(CompanyLocation_list)):
  CompanyLocation.append(CompanyLocation_list[i].get_text())
#print(CompanyLocation)

#BeanType
BeanType = []
BeanType_list = soup.select(".BeanType")
#print(BeanType_list)
for i in range(1,len(BeanType_list)):
  BeanType.append(BeanType_list[i].get_text())
#print(BeanType)

#BroadBeanOrigin
BroadBeanOrigin = []
BroadBeanOrigin_list = soup.select(".BroadBeanOrigin")
#print(BroadBeanOrigin_list)
for i in range(1,len(BroadBeanOrigin_list)):
  BroadBeanOrigin.append(BroadBeanOrigin_list[i].get_text())
#print(BroadBeanOrigin)

#Creating an empty dataframe to store all the lists
df = pd.DataFrame()
#adding all the columns inside the dataframe
df['Company'] = Company
df['Origin'] = Origin
df['REF'] =REF
df['ReviewDate'] = ReviewDate
df['CocoaPercent'] =CocoaPercent
df['CompanyLocation'] = CompanyLocation
df['Rating']=Rating
df['BeanType'] =BeanType
df['BroadBeanOrigin'] = BroadBeanOrigin

#df['CocoaPercent'] = (df['CocoaPercent'].str.replace('%',''))
df['CocoaPercent'] = df['CocoaPercent'].str.replace('%', '').str.replace('$', '').astype(float)


#print(df.head())
#print(df.columns)
print(df.info())

#finding total rating of each company
total_ratings = df.groupby('Company').Rating.sum().reset_index()
#print(total_ratings)

#Highest 10 rating companies
largest_10 = total_ratings.nlargest(10,'Rating')
print(largest_10)

#Scatter plot between CocoaPercent and rating
plt.scatter(df.CocoaPercent, df.Rating)
#best-fit line in scatterplot
z = np.polyfit(df.CocoaPercent, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercent, line_function(df.CocoaPercent), "r--")
plt.show()
plt.clf()

#storing the file in CSV file format
df.to_csv('chocolate.csv', encoding='utf-8')
