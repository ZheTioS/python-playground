import xml.etree.ElementTree as ET 
import urllib.request, urllib.parse, urllib.error
# Extra steps to be taken in case of SSL

# Sample URL : http://py4e-data.dr-chuck.net/comments_42.xml
# Actual URL : http://py4e-data.dr-chuck.net/comments_1095118.xml
serviceurl = 'http://py4e-data.dr-chuck.net/comments_1095118.xml'

print('Retrieving', serviceurl) # To display the link used to retrieve data from
handle = urllib.request.urlopen(serviceurl) #to save data from URL as a file
data = handle.read() #to read file
print('Retrieved', len(data), 'characters') #to print no.of characters in the retrieved file
tree = ET.fromstring(data) # Creates xml tree out of data

counts =  tree.findall('.//count') # to find tag : count
print ("Count: " + str(len(counts))) # to print no.of tags found

x = 0 # counter variable

for count in counts: # to go thru data and retrive the txt
    x += int(count.text) # to add with each counter

print ("Sum:" + str(x)) #Print sum