from collections import Counter

from pysam import FastaFile

from rosalind.utils import get_data_file


def calc_gc_content(sequence):
    count = Counter(sequence)
    return (count["G"] + count["C"]) / len(sequence)


def get_largest_gc_content(fasta):
    gc_content = {
        reference: calc_gc_content(fasta.fetch(reference))
        for reference in fasta.references
    }
    max_key = max(gc_content, key=gc_content.get)
    return max_key, gc_content[max_key] * 100


def test():
    fasta = FastaFile(get_data_file("rosalind_gc_test.txt"))
    reference, gc_content = get_largest_gc_content(fasta)
    print(reference)
    print(gc_content)


def main():
    fasta = FastaFile(get_data_file("rosalind_gc.txt"))
    reference, gc_content = get_largest_gc_content(fasta)
    print(reference)
    print(gc_content)


if __name__ == "__main__":
    # test()
    main()
