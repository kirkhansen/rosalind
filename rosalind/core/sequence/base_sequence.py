"""
>>> BaseSequence('ABCDEFGHIJKLMNOP')
BaseSequence(sequence='ABCDEFGHIJ...')
"""
from collections import OrderedDict

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import Alphabet
from itertools import product


from rosalind.core.sequence.exception import InvalidSequenceCharacterError
from rosalind.core.util import overlapping_occurrences


class BaseSequence(object):
    def __init__(self, sequence, sequence_type=Alphabet()):
        self._sequence = Seq(sequence, sequence_type)
        self.letters = None
        self.__validate_sequence()

    def __validate_sequence(self):
        if self._sequence.alphabet.letters:
            invalid_nucleotides = [letter for letter in self._sequence if letter not in self._sequence.alphabet.letters]
            if invalid_nucleotides:
                raise InvalidSequenceCharacterError(
                    "Invalid sequence passed. Offending characters: {}".format("".join(invalid_nucleotides))
                )
            self.letters = self._sequence.alphabet.letters

    def __repr__(self):
        class_name = self.__class__.__name__
        return "{}(sequence='{}')".format(class_name, ''.join(self._sequence[:10]) + "...")

    def __str__(self):
        return str(self._sequence)

    def __len__(self):
        return len(self._sequence)

    def transcribe(self):
        return self._sequence.transcribe()

    def translate(self):
        return self._sequence.translate()

    def get_kmer_composition(self, k):
        """
        Returns an ordered dict of the kmer composition where the keys are the k-mer,
        and the values ore the number of occurrences
        """
        perms = product(sorted(self.letters), repeat=k)

        kmers = OrderedDict()
        for perm in perms:
            kmer = ''.join(perm)
            if kmer not in kmers:
                # str.count does not see overlaps
                kmers[kmer] = str(overlapping_occurrences(str(self), kmer))
        return kmers


    @classmethod
    def many_from_file(cls, file_handle, file_format):
        for record in SeqIO.parse(file_handle, file_format):
            yield cls(str(record.seq))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
