"""
>>> RNA('ABCDEFGHIJKLMNOP')
Traceback (most recent call last):
    ...
InvalidSequenceCharacterError: Invalid sequence passed. Offending characters: BDEFHIJKLMNOP

>>> RNA('GTGCATCGATTAGAAAA')
Traceback (most recent call last):
    ...
InvalidSequenceCharacterError: Invalid sequence passed. Offending characters: TTTT

>>> RNA('GUGCAUCGAUUAGAAAA')
RNA(sequence='GUGCAUCGAU...')
"""
from Bio.Alphabet import IUPAC

from rosalind.core.sequence.base_sequence import BaseSequence


class RNA(BaseSequence):
    def __init__(self, sequence):
        super(RNA, self).__init__(sequence, IUPAC.unambiguous_rna)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
