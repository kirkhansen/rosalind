"""
>>> BaseSequence('ABCDEFGHIJKLMNOP')
BaseSequence(sequence='ABCDEFGHIJ...')
"""
from Bio import SeqIO
from Bio.Seq import Seq


class BaseSequence(object):
    def __init__(self, sequence, sequence_type=None):
        self.sequence = Seq(sequence, sequence_type)

    def __repr__(self):
        class_name = self.__class__.__name__
        return "{}(sequence='{}')".format(class_name, ''.join(self.sequence[:10]) + "...")

    @classmethod
    def many_from_file(cls, file_handle, file_format):
        for record in SeqIO.parse(file_handle, file_format):
            yield cls(record.sequence)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
