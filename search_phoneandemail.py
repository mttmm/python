#! python3
import re, pyperclip

# Create a regex for phone numbers

phoneRegex = re.compile (r'''
        # phone number types 415-555-0000, (415) 555-0000, 555-0000, ext 12345, ext. 12345, x12345

(               # wraps all the regex into one group instead of individual tuples
((\d\d\d) | (\(\d\d\d\)))? # area code (optional) "?" means the syntax can occur 0 or 1 times (optional). the second group is escaping the paren with (\(\d\d\d\))
(\s | -) # first separator. looking for a space (\s) or a dash
\d\d\d # first 3 digits
 - # separator
\d\d\d\d # last 4 digits
(((ext(\.)?\s) | x)    # extension word-part (optional). looking for the word 'ext' and a literal period (\.) or the letter 'x' (| x)
(\d{2,5}))?    # extension number-part (optional). looking for a digit between 2-5 characters long and is optional
)          # closes the regex group wrap
''', re.VERBOSE) # re.VERBOSE allows the regex pattern to be multiline and supports comments

# Create a regex for email address 

emailRegex = re.compile(r'''
          # Email types: some.+_thing@some.+thing. (.com, .org, .edu)

[a-zA-Z0-9_.+]+    #name part.  creating a character class looking for upper and lower case letters, numbers 0-9, underscores, periods, or plus signs. the plus sign outside of the class block is looking for one or more
@                  # @ symbol
[a-zA-Z0-9_.+]+    # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()    # Returns the string text that is currently on the clipboard

 # Extract the email/phone from the text in the clipboard
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)

 