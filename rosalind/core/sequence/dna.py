"""
>>> DNA('ABCDEFGHIJKLMNOP')
DNA(sequence='ABCDEFGHIJ...')
"""
from Bio.Alphabet import IUPAC

from rosalind.core.sequence.base_sequence import BaseSequence


class DNA(BaseSequence):
    def __init__(self, sequence):
        super(DNA, self).__init__(sequence, IUPAC.unambiguous_dna)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

