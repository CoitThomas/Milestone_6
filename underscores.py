"""Take input from a user and print out the given input with the white
space between words replaced by an underscore."""

from get_input import get_input

def replace_space(string):
    """Replace all the whitespace found in a given string with an
    underscore and return it.
    """
    words_list = string.split()
    return '_'.join(words_list)

if __name__ == "__main__":
    INPUT = get_input()
    print replace_space(INPUT)
