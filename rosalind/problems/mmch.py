from rosalind.core.sequence.nucleotide.rna import RNA
from rosalind.problems.util import get_data_file_path

for dna_sequence in RNA.many_from_file(get_data_file_path('mmch'), 'fasta'):
    print dna_sequence


