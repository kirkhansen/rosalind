import os

from rosalind.core.common.constants import DATA_DIR
from rosalind.core.sequence.dna import DNA

for dna_sequence in DNA.many_from_file(os.path.join(DATA_DIR, 'rosalind_kmer.txt'), 'fasta'):
    print ' '.join(dna_sequence.get_kmer_composition(4).values())
