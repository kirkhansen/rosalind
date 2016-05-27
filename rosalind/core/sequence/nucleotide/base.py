from rosalind.core.sequence.base_sequence import BaseSequence


class Base(BaseSequence):
    def __init__(self, sequence, sequence_type):
        super(Base, self).__init__(sequence, sequence_type)
        self.pairs = set()

    def get_nucleotide_pair_count(self):
        """
        Counts up the number of each pair mapping
        :return:  dict
        """
        pair_counts = {pair: [str(self).count(nucleotide) for nucleotide in pair] for pair in self.pairs}
        return pair_counts

