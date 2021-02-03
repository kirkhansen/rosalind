from collections import defaultdict

from pysam import FastaFile

from rosalind.utils import get_data_file

def get_consensus_string(profile_dict):
    consensus_string = ""
    total_bp = len(profile_dict["A"])
    bps = list(profile_dict.keys())
    for i in range(total_bp):
        col = {key: profile_dict[key][i] for key in bps}
        consensus_string += max(col, key=col.get)
    return consensus_string

def get_profile_dict(matrix):
    num_cols = len(matrix[0])
    profile = {
        "A": [0] * num_cols,
        "C": [0] * num_cols,
        "G": [0] * num_cols,
        "T": [0] * num_cols,
    }
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            profile[matrix[j][i]][i] += 1
    return profile


def pprint_profile_dict(profile_dict):
    for key in profile_dict.keys():
        print(f"{key}: {' '.join(str(v) for v in profile_dict[key])}")


def create_dna_matrix(fasta):
    return [
        [bp for bp in fasta.fetch(reference)]
        for reference in fasta.references
    ]


def main():
    fasta = FastaFile(get_data_file("rosalind_cons.txt"))
    matrix = create_dna_matrix(fasta)
    profile_dict = get_profile_dict(matrix)
    print(get_consensus_string(profile_dict))
    pprint_profile_dict(profile_dict)


if __name__ == "__main__":
    main()

