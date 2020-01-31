import pandas as pd
import requests
from bs4 import BeautifulSoup

page  = requests.get('https://forecast.weather.gov/MapClick.php?lat=36.37410569300005&lon=-119.27022999999997')
#BeautifulSoup makes the web scrapping easy it give you nice struture. it able to find element tags from HTML page
soup = BeautifulSoup(page.content, 'html.parser')
#creating variable for the entire table div.
week = soup.find(id='seven-day-forecast-body')
#print(week)
#storing div container which contain data about weather!
items = week.find_all(class_="tombstone-container")
#print(items[0])
#getting text from each of the class.
# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())
#list comprehension to get all the needs.
period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

# print(period_names)
# print(short_description)
# print(temperatures)
#inserting all the values in one column
weather_stuff = pd.DataFrame({'period': period_names,'short_description': short_description,'temperatures': temperatures,})

print(weather_stuff)
#converting to csv file
weather_stuff.to_csv('weather.csv')