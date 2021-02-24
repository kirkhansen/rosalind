from pysam import FastxFile

from rosalind.problems.revc import reverse_complement
from rosalind.utils import get_data_file


def get_reverse_palindromes(sequence):
    reverse_palindromes = []
    for i in range(len(sequence) + 1):
        for j in range(i, len(sequence) + 1):
            sub_sequence = sequence[i:j]
            revc = reverse_complement(sub_sequence)
            sub_sequence_len = len(sub_sequence)
            if sub_sequence == revc and sub_sequence_len >= 4 and sub_sequence_len <= 12:
                reverse_palindromes.append((i + 1, len(sub_sequence)))
    return reverse_palindromes


def test():
    sequence = next(FastxFile(str(get_data_file("rosalind_revp_test.txt")))).sequence
    for rp in get_reverse_palindromes(sequence):
        print(" ".join(str(i) for i in rp))


def main():
    sequence = next(FastxFile(str(get_data_file("rosalind_revp.txt")))).sequence
    for rp in get_reverse_palindromes(sequence):
        print(" ".join(str(i) for i in rp))


if __name__ == "__main__":
    # test()
    main()
