
# Automation

[Link to Latest PR](https://github.com/ticochuck/automation/pull/2)
                   
## Description
- Devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.

## Feature Tasks and Requirements

- Given a document potential-contacts, find and collect all email addresses and phone numbers.
- Phone numbers may be in various formats.
    - (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
    - phone numbers with missing area code should presume 206
    - phone numbers should be stored in xxx-yyy-zzzz format.
- Once emails and phone numbers are found they should be stored in two separate documents.
- The information should be sorted in ascending order.
- Duplicate entries are not allowed.



## User Acceptance Tests

- The ‘phone_numbers.txt’ and ‘emails.txt’ files will be verified by an automated system. So make sure to match the naming/formatting requirements exactly.

## References

[MadLib](https://github.com/ticochuck/madlib-cli/blob/master/madlib_cli/madlib.py)


[Email Regex](https://www.geeksforgeeks.org/extracting-email-addresses-using-regular-expressions-python/)


[Phone Number Regex](https://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script)

    (\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})

[Phone Number Formatter](https://stackoverflow.com/questions/7058120/whats-the-best-way-to-format-a-phone-number-in-python)

    clean_phone_number = re.sub('[^0-9]+', '', phone_number)
    formatted_phone_number = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(clean_phone_number[:-1])) + clean_phone_number[-1]

## Lab19 - Automation

[Canvas Assignment](https://canvas.instructure.com/courses/2045906/assignments/15160042)

## Author

[Chuck Li Villalobos](https://github.com/ticochuck)
