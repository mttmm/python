import re
message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # r' is to tell python a raw string follows. Parenths around the raw string will separate string into groups

phoneNumRegex.search(message)

mo = phoneNumRegex.search(message) # mo stands for matched object

print (mo.group(1)) #prints group 1
print (mo.group(2)) #prints group 2

message2 = 'Batmobile lost its wheel'
batRegex = re.compile (r'Bat(man|mobile|copter)') # the pipe can be used to match one of many possible groups
mo2 = batRegex.search(message2)
print (mo2.group())
