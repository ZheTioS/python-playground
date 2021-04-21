import socket #To use the built-in network support

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates an unconncected socket
mysock.connect (('data.pr4e.org',80)) #Connects socket to required host domain

#The HTTP command to access the required info.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #encode is used to convert unicode to UTF-8
#usually \n\n is used. Incase that fails, use \r\n\r\n
mysock.send(cmd) #sends the command out

while True:
    data = mysock.recv(512) #loop to request 512 characaters
    if (len(data) < 1): #if file is at EOF it stops here
        break
    print(data.decode())

mysock.close() #close socket