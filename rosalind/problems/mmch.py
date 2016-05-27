from rosalind.core.sequence.nucleotide.rna import RNA
from rosalind.problems.util import get_data_file_path, get_output_file_path
from math import factorial

NAME = 'mmch'


def num_permutations(max_pairs, min_pairs):
    return factorial(max_pairs) / factorial(max_pairs - min_pairs)


for rna in RNA.many_from_file(get_data_file_path(NAME), 'fasta'):
    counts = rna.get_nucleotide_pair_count()
    maximum_number_of_matchings = num_permutations(max(counts['AU']), min(counts['AU'])) * \
             num_permutations(max(counts['GC']), min(counts['GC']))

    print maximum_number_of_matchings

    with open(get_output_file_path(NAME), 'w') as outfile:
        outfile.write(str(maximum_number_of_matchings))
