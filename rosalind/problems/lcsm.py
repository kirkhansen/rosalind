from pysam import FastaFile

from rosalind.utils import get_data_file


def motif_in_all_sequences(motif, sequences):
    return all(motif in sequence for sequence in sequences)

def longest_common_substring(fasta):
    # This could be done much more efficiently I think.
    # Feels ripe for a binary search
    done = False
    longest_common_substring = ""
    sequences = [fasta.fetch(reference) for reference in fasta.references]
    for i in range(len(sequences[0])):
        for j in range(len(sequences[0])):
            motif = sequences[0][i:j]
            if motif_in_all_sequences(motif, sequences) and len(motif) > len(longest_common_substring):
                longest_common_substring = motif
    return longest_common_substring


def test():
    fasta = FastaFile(get_data_file("rosalind_lcsm_test.txt"))
    expected = "TA"
    assert longest_common_substring(fasta) == expected

def main():
    fasta = FastaFile(get_data_file("rosalind_lcsm.txt"))
    print(longest_common_substring(fasta))


if __name__ == "__main__":
    main()
