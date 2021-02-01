from collections import Counter

from rosalind.utils import get_data_file


def count_nucleotides(sequence):
    count = Counter(sequence)
    print(count["A"], count["C"], count["G"], count["T"])
    return count


def test():
    s_input = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    count_nucleotides(s_input)


if __name__ == "__main__":
    with get_data_file("rosalind_dna.txt").open() as f:
        count_nucleotides(f.readline())
