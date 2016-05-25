"""
>>> DNA('ABCDEFGHIJKLMNOP')
Traceback (most recent call last):
    ...
InvalidSequenceCharacterError: Invalid sequence passed. Offending characters: BDEFHIJKLMNOP

>>> DNA('GTGCATCGATTAGAAAA')
DNA(sequence='GTGCATCGAT...')
"""
from Bio.Alphabet import IUPAC

from rosalind.core.sequence.base_sequence import BaseSequence


class DNA(BaseSequence):
    def __init__(self, sequence):
        super(DNA, self).__init__(sequence, IUPAC.unambiguous_dna)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
