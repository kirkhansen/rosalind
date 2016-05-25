from Bio.Alphabet import IUPAC

from rosalind.core.sequence.base_sequence import BaseSequence


class RNA(BaseSequence):
    def __init__(self, sequence):
        super(RNA, self).__init__(sequence, IUPAC.unambiguous_rna)
