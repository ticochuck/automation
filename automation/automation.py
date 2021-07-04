from datetime import datetime
import re

dateTimeObj = datetime.now()

def open_file(path, file):

    full_path = path + file
    try:

        with open(full_path, 'r') as potential_contacts:
            contents = potential_contacts.read()

            find_emails(contents)
            find_phone_numbers(contents)


    except FileNotFoundError as err:
        with open('assets/error_log.txt', 'a') as error_log:
            error_log.write(f'\nFile does not exits error: \n{err}\n{str(dateTimeObj)}\n')

def find_emails(contents):
    emails = re.findall(r'\S+@\S+', contents)
    emails.sort()
    unique = []
    
    for email in emails:
        if email not in unique:
            unique.append(email)
        
    email_file(unique)


def find_phone_numbers(contents):
    phones = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', contents)
    phones.sort()
    unique_numbers = []
    
    for p_number in phones:
            
        digits_only = re.sub('[^0-9]+', '', p_number)
        correct_format = re.sub(r"(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(digits_only[:-1])) + digits_only[-1]
        if len(correct_format) < 12:
            correct_format = '206' + correct_format[2:]

        if correct_format not in unique_numbers:
            unique_numbers.append(correct_format)

    unique_numbers.sort()
    phone_number_file(unique_numbers)
    

def email_file(emails):
    
    with open('./assets/emails.txt', 'w') as emails_file:
        for email in emails:
            emails_file.write(f'{email}\n')


def phone_number_file(phone_numbers):
    
    with open('./assets/phone_numbers.txt', 'w') as phone_numbers_file:
        for phone_number in phone_numbers:
            phone_numbers_file.write(f'{phone_number}\n')



def main():
    """
    Main funtion. Assigns values to path and file_name variables.
    Calls the open_file() to read a file

    """
    path = './assets/'
    file_name = 'potentialcontacts.txt'
    open_file(path, file_name)


    
if __name__ == '__main__':
    main()
    


