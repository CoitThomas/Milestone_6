"""Verify if the function generate_acronym returns the correct string."""

from acronym import generate_acronym

def test_generate_acronym():
    """Assert if generate_acronym returns the correct acronym for a
    given string."""
    assert generate_acronym('Hello my baby. Hello my honey. Hello my rag time gal.'
                           ) == 'HMBHMHHMRTG'
    assert generate_acronym('Testing, testing, 1, 2, 1, 2.') == 'TT1212'
    assert generate_acronym('World War 2') == 'WW2'
