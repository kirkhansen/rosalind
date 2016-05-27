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

    def __iter__(self):
        return iter(self._sequence)

    def __getitem__(self, item):
        return self._sequence[item]

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

    def get_failure_array(self):
        """
        Generate a failure array for the given dna sequence to be use with the KMP search.
        :return: list
        """
        i = 0
        # seed fails with 0
        failure_array = [0] * len(self)

        for m in range(2, len(self)):
            while i > 0 and self[i] != self[m - 1]:
                i = failure_array[i - 1]
            if self[i] == self[m - 1]:
                i += 1
            failure_array[m - 1] = i

        return failure_array

    @classmethod
    def many_from_file(cls, file_handle, file_format):
        for record in SeqIO.parse(file_handle, file_format):
            yield cls(str(record.seq))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
