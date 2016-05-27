import os

from rosalind.core.common.constants import DATA_DIR
from rosalind.core.sequence.dna import DNA


for dna_sequence in DNA.many_from_file(os.path.join(DATA_DIR, 'rosalind_kmp.txt'), 'fasta'):
    print ' '.join(map(str, dna_sequence.get_failure_array()))
