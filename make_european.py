"""Take input in the format:
mm/dd/yyyy:username@host
Print out all of the usernames that have the host 'aol' and convert
the date to European format so that the following format is produced:
dd/mm/yyyy username
"""
import re

def get_input():
    """Prompts the user for input in the format:
    mm/dd/yyyy:username@host
    Receive the input as raw_input.
    """
    try:
        return raw_input()
    except EOFError:
        return ' '

def convert_input(string, desired_host):
    """Take in a string and a desired host. If the host found in the
    string matches the desired host, then convert the found date to the
    European format and return the new date and username.
    """
    username, host = find_email_address(string)
    if host == desired_host:
        month, day, year = find_date(string)
        euro_date = make_european(month, day, year)
        return '%s %s' % (euro_date, username)

def find_email_address(string):
    """Take in a string and return the username and host of the email
    address found in the string.
    """
    email_address = re.search(r'([\w.-]+)@([\w.-]+)', string)
    assert email_address, "A proper email address must be provided."
    return (email_address.group(1), email_address.group(2))

def find_date(string):
    """Take in a string and return the month, day, and year of the date
    found in the string."""
    date = re.search('([0-9]{1,2})/([0-9]{1,2})/([0-9]{4})', string)
    assert date, "A date in the format mm/dd/yyyy must be provided."
    return (date.group(1), date.group(2), date.group(3))

def make_european(month, day, year):
    """Take in a month, day, and year, and return those elements in the
    European format:
    dd/mm/yyyy
    """
    return '%s/%s/%s' % (day, month, year)

if __name__ == "__main__":
    INPUT = get_input()
    while not INPUT.isspace() and INPUT:
        VALID_OUTPUT = convert_input(INPUT, 'aol.com')
        if VALID_OUTPUT:
            print VALID_OUTPUT
        INPUT = get_input()
