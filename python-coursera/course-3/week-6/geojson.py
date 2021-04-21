import json
import urllib.request, urllib.error, urllib.parse

serviceurl = 'http://py4e-data.dr-chuck.net/json?' #url provided
api_key = 42 #API Key required to run

while True:
    address = input('Enter location: ') #To enter location
    if len(address) < 1: break #To exit loop

    parms = dict() # Create a dictionary to story parameters
    parms['address'] = address #adding address to parameter
    if api_key is not False: parms['key'] = api_key #adding key to parameters
    
    # It should be noted that key must go before address for testing sample, hint obtained from forum
    url = serviceurl + urllib.parse.urlencode(parms) #Creating url for req
    print('Retrieving', url)# To display the link used to retrieve data from
    uh = urllib.request.urlopen(url)#to save data from URL as a file
    data = uh.read().decode() #to read file
    print('Retrieved', len(data), 'characters') # displays obtained char

    try:
        js = json.loads(data)#to obtain json object
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':#to check if all parameters are good
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    #if js["results"][0]["place_id"] == "ChIJLzabHQ7i2IgRzeZb_AgUj0Q": #Used for testing sample
    print ("Place id: ", js["results"][0]["place_id"])
    #else:
     #   print ("Place_ID does not match")