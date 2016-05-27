from rosalind.core.sequence.base_sequence import BaseSequence


class Base(BaseSequence):
    def __init__(self, sequence, sequence_type):
        super(Base, self).__init__(sequence, sequence_type)
        self.pairs = {}
