"""Take input from a user and print out the given input with the white
space between words replaced by an underscore."""

def get_input():
    """Propmt the user for input and store it as a string."""
    return raw_input("Enter whatever your heart desires:")

def replace_space(input):
    """Replace all the whitespace found in a given string with an
    underscore and return it.
    """
    words_list = input.split()
    return '_'.join(words_list)

if __name__ == "__main__":
    INPUT = get_input()
    print replace_space(INPUT)
