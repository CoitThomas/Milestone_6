"""Verify if the function replace_space returns the correct string."""

from underscores import replace_space

def test_replace_space():
    """Assert whether or not the white space in between words is
    replaced with underscores.
    """
    assert replace_space('I like to eat, eat, eat, apples and bananas.'
                        ) == 'I_like_to_eat,_eat,_eat,_apples_and_bananas.'
    assert replace_space('Hello.') == 'Hello.'
    assert replace_space('1 2 3') == '1_2_3'
