from collections import defaultdict

from rosalind.utils import get_data_file
from rosalind.problems.prot import RNA_CODON_STRING


def get_rna_frequencies():
    rna_frequencies = defaultdict(int)
    for code in RNA_CODON_STRING.split()[1::2]:
        rna_frequencies[code] += 1
    return rna_frequencies


def rna_combination_count(prot, mod=1_000_000):
    # I'd like to do this, but the problem suggests the point is
    # the number may breach the int data types capabilities.
    # frequencies = get_rna_frequencies()
    # num_rna_possibilities = math.prod(int(frequencies[code]) for code in prot)
    # num_rna_possibilities *= frequencies["Stop"]
    # return num_rna_possibilities % mod
    # instead, we'll loop through and mod each result by 1_000_000
    # to reset the counter
    frequencies = get_rna_frequencies()
    num_rna_possibilities = frequencies["Stop"]
    for code in prot:
        num_rna_possibilities = (num_rna_possibilities * frequencies[code]) % 1_000_000
    return num_rna_possibilities


def test():
    prot = "MA"
    assert rna_combination_count(prot) == 12
    print("PASS")


def main():
    with get_data_file("rosalind_mrna.txt").open() as f:
        prot = f.readline().rstrip()
    print(rna_combination_count(prot))


if __name__ == "__main__":
    # test()
    main()
