"""
>>> DNA('ABCDEFGHIJKLMNOP')
Traceback (most recent call last):
    ...
InvalidSequenceCharacterError: Invalid sequence passed. Offending characters: BDEFHIJKLMNOP

>>> DNA('GTGCATCGATTAGAAAA')
DNA(sequence='GTGCATCGAT...')
"""
from Bio.Alphabet import IUPAC

from rosalind.core.sequence.nucleotide.base import Base


class DNA(Base):
    def __init__(self, sequence):
        super(DNA, self).__init__(sequence, IUPAC.unambiguous_dna)
        self.pairs = {'AT', 'GC'}

if __name__ == '__main__':
    import doctest
    doctest.testmod()
