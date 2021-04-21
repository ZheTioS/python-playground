import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#In case of SSL security issues for HTTPS:// sites few extra steps need to be taken

#test code with sample data
#Sample Url : http://py4e-data.dr-chuck.net/comments_42.html
# url_sample = input("Enter Url :") #Sample Url
# html_sample = urllib.request.urlopen(url_sample).read() # for sample
# soup_sample = BeautifulSoup(html_sample, 'html.parser')
# spans = soup_sample('span')

#Actual URL : http://py4e-data.dr-chuck.net/comments_1095116.html
url = input("Enter Url :") 
html = urllib.request.urlopen(url).read() #Reading the HTML code from the given URL
soup = BeautifulSoup(html, 'html.parser') #Using beautiful soup to parse the obtained file
spans = soup('span') # Asigning the tag to be found

numbers = [] # Creating a list to store numbers obtained

for span in spans: #for loop to traverse through the parsed html file
    numbers.append(int(span.string)) #obtaining the numbers from parsed file

print (sum(numbers)) #printing the sum of numbers obtained