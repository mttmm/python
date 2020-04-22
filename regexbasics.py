import re #regular expression module

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # r' is to tell python a raw string follows

mo = phoneNumRegex.search(message) # mo stands for matched object
print(mo.group()) # prints the first occurance of the matched object

print(phoneNumRegex.findall(message)) # prints all matched objects in the message