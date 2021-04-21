#Code written by Vinayak Nair for Using Python to Access Web Data coursera course

import json
import urllib.request, urllib.parse, urllib.error
# Extra steps to be taken in case of SSL
# Created by modifying the xml script

# Sample URL : http://py4e-data.dr-chuck.net/comments_42.json
# Actual URL : http://py4e-data.dr-chuck.net/comments_1095119.json
serviceurl = 'http://py4e-data.dr-chuck.net/comments_1095119.json'

print('Retrieving', serviceurl) # To display the link used to retrieve data from
handle = urllib.request.urlopen(serviceurl) #to save data from URL as a file
data = handle.read() #to read file
print('Retrieved', len(data), 'characters') #to print no.of characters in the retrieved file
jd = json.loads(data) # takes json data

info = jd['comments'] # to find tag : comments

x = 0 # counter variable for sum
y = 0 # to count instances of "count"

for item in info:
    x += int(item["count"]) #adding sum
    y +=1 #for counter

print("Count:" + str(y)) #Print instances found
print ("Sum:" + str(x)) #Print sum