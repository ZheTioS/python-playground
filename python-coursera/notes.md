# Notes for coursera python course
# Using python to access web data
## Week 2 - Regular Expressions
Regular expressions cheat sheet

| Expression 	| Description 	|
|-	|-	|
| ^ 	| Matches the beginning of a line 	|
| $ 	| Matches the end of the line 	|
| . 	| Matches any character 	|
| \s 	| Matches whitespace 	|
| \S 	| Matches any non-whitespace character 	|
| * 	| Repeats a character zero or more times 	|
| *? (non-greedy)	| Repeats a character zero or more times 	|
| + 	| Repeats a character one or more times 	|
| +? (non-greedy)	| Repeats a character one or more times 	|
| [aeiou] 	| Matches a single character in the listed set 	|
| [^XYZ] 	| Matches a single character not in the listed set 	|
| [a-z0-9] The set of characters can include a range 	|  	|
| ( 	| Indicates where string extraction is to start 	|
| ) 	| Indicates where string extraction is to end 	|

More info can be found [here](https://docs.python.org/3/howto/regex.html)

## Week 3 - Networked Technology
* An internet socket or network socket is an endpoint of a bidirectional inter-process communication flow across an Internet Protocol-based computer network, such as the Internet
* A port is defined as an application-specific or process-specific software communications endpoint

Ports that will be of focus for this module are
- Port 80 which is the web port (HTTP)
- Port 443 which is for secure HTTPS

Other common TCP ports include
- Telnet (23) - login
- SSH (22) - Secure login
- SMTP (25) - Mail
- IMAP(143/220/993) - Mail Retrieval
- POP(109/110) - Mail Retrieval
- DNS (53) - Domain Name
- FTP (21) - File Transfer

Python has requires 3 lines of code to use these ports

```python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect (('data.pr4e.org',80))
```
In the above snippet we use the built in support for TCP sockets and can connect by passing in the host and port as arguments.

"socket.SOCK_STREAM" creates an endpoint on the computer that is read to connect out, but is not yet connected.

Hypertext Transfer Protocol (HTTP) is the dominant Application Layer Protocol on the Internet. It was invented for the Web - to retrieve HTML, Images, etc.

A Protocol is defined as a set of rules that all parties follow so we can predict each other's behaviour and not bump into each other.