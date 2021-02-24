from itertools import islice

from pysam import FastxFile

from rosalind.problems.revc import reverse_complement
from rosalind.problems.prot import grouper
from rosalind.utils import get_data_file


DNA_CODON_TABLE = {
    "TTT": "F",
    "CTT": "L",
    "ATT": "I",
    "GTT": "V",
    "TTC": "F",
    "CTC": "L",
    "ATC": "I",
    "GTC": "V",
    "TTA": "L",
    "CTA": "L",
    "ATA": "I",
    "GTA": "V",
    "TTG": "L",
    "CTG": "L",
    "ATG": "M",
    "GTG": "V",
    "TCT": "S",
    "CCT": "P",
    "ACT": "T",
    "GCT": "A",
    "TCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "TCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "TCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "TAT": "Y",
    "CAT": "H",
    "AAT": "N",
    "GAT": "D",
    "TAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "TAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "TAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "TGT": "C",
    "CGT": "R",
    "AGT": "S",
    "GGT": "G",
    "TGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "TGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "TGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def translate_dna_codon(codon):
    return DNA_CODON_TABLE.get("".join(codon), None)


def translate_sequence(seq):
    prot_gen = (translate_dna_codon(codon) for codon in grouper(3, seq, "x"))
    protein_string = ""
    for prot in prot_gen:
        if prot == "Stop":
            return protein_string
        elif prot:
            protein_string += prot
        else:
            return None
    return None


def get_start_codon_indicies(seq):
    prot_gen = (translate_dna_codon(codon) for codon in window(seq, 3))
    for index, prot in enumerate(prot_gen):
        if prot == "M":
            yield index


def _protein_strings_for_sequence(dna_sequence):
    start_indicies = get_start_codon_indicies(dna_sequence)
    for start_index in start_indicies:
        protein = translate_sequence(dna_sequence[start_index:])
        if protein:
            yield protein


def possible_protein_seqs(dna_sequence):
    for protein in _protein_strings_for_sequence(dna_sequence):
        yield protein
    for protein in _protein_strings_for_sequence(reverse_complement(dna_sequence)):
        yield protein


def test():
    from pprint import pprint

    dna_seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    expected = set(
        [
            "MLLGSFRLIPKETLIQVAGSSPCNLS",
            "M",
            "MGMTPRLGLESLLE",
            "MTPRLGLESLLE",
        ]
    )
    result = set(possible_protein_seqs(dna_seq))
    if expected != result:
        print("expected", expected)
        print("result", result)
        assert False
    print("PASS")


def main():
    sequence = next(FastxFile(str(get_data_file("rosalind_orf.txt")))).sequence

    for protein in set(possible_protein_seqs(sequence)):
        print(protein)


if __name__ == "__main__":
    # test()
    main()
