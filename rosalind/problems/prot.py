from itertools import zip_longest
from rosalind.utils import get_data_file

# Given by Rosalind
RNA_CODON_STRING = """
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G
"""
_flat = RNA_CODON_STRING.split()
# zip dna code 'keys' with protein code 'values'
RNA_CODON_LOOKUP = dict(zip(_flat[0::2], _flat[1::2]))


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def translate_sequence(sequence):
    translation = ""
    for code in grouper(3, sequence):
        protein_code = RNA_CODON_LOOKUP["".join(code)]
        if protein_code != "Stop":
            translation += protein_code
    return translation


def test():
    sequence = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    expected = "MAMAPRTEINSTRING"
    translation = translate_sequence(sequence)
    print(translation)
    assert translation == expected
    print("PASS")


def main():
    with get_data_file("rosalind_prot.txt").open() as f:
        sequence = f.readline().rstrip()
    translation = translate_sequence(sequence)
    print(translation)


if __name__ == "__main__":
    # test()
    main()
