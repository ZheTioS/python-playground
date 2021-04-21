import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#In case of SSL security issues for HTTPS:// sites few extra steps need to be taken


# Sample url : http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Actual url : http://py4e-data.dr-chuck.net/known_by_Digby.html

url = input("Enter URL: ") # To accept URL
count = int(input("Enter count: ")) # No.of times the code must crawl
position = int(input("Enter position: ")) # Starting position of link


names = [] # Creating empty list of names

while count > 0: 
    print ("retrieving: {0}".format(url)) # to display file being retrieved
    html = urllib.request.urlopen(url).read() # to open the retrieved file
    soup = BeautifulSoup(html, "html.parser") #parsing html file
    anchors = soup('a') # Defining the anchor to be used
    name = anchors[position-1].string #Obtaining the name from the Given position
    names.append(name) #adding the names to the list
    url = anchors[position-1]['href'] # Redefining the desired positioned url as the new url for running the loop for desired times
    count -= 1 #reducing count

print (names[-1]) #Printing the last name on the list