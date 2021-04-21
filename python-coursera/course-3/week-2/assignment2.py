#Code written by Vinayak Nair for Using Python to Access Web Data coursera course

import re #invoking regular expression module

#Opening the file(s) in which we'll need to find the numbers
sample_file = open('regex_sum_42.txt') #This is to open the sample file
actual_file = open('regex_sum_1095114.txt') #This is to open the actual file

#Obtaining strings representing the numbers in that file(s)
text = sample_file.read()
actual_text = actual_file.read() #With read, we read the entire text and not line by line
number_regex = '[0-9]+' #we define the expression
sample_no = re.findall(number_regex, text) #Match any combination of one or more digits
actual_no = re.findall(number_regex, actual_text) #for actual text
#Casting them to integers and getting the total sum
sample_total = sum(int(num) for num in sample_no) #sample text
if sample_total == 445833: #Checking if the calculated total of sample text matches value given in assignment
    actual_total = sum(int(num) for num in actual_no)
    print('The sum from the actual data is',actual_total)
else:
    print('The total of sample text does not match given sample total. The total calculated is',sample_total)

#Closing the file to avoid memory problems
sample_file.close()
actual_file.close()