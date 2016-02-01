"""Take input from a user and print the corresponding acronym."""

from get_input import get_input

def generate_acronym(string):
    """Create an acronym from a given string input and return it."""
    words = string.split()
    letters = []
    for word in words:
        letters.append(word[0])
    acronym = ''.join(letters)
    return acronym.upper()

if __name__ == "__main__":
    INPUT = get_input()
    print generate_acronym(INPUT)
