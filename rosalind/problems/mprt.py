import re
import tempfile

import requests
from pysam import FastxFile

from rosalind.utils import get_data_file

HOST = "https://www.uniprot.org"
UNIPROT_BASE_URI = f"{HOST}/uniprot"


def fetch_protein_fasta(access_id):
    res = requests.get(f"{UNIPROT_BASE_URI}/{access_id}.fasta")
    if res.status_code == 300:
        res = requests.get(f"{HOST}{res.headers['Location']}")
    return res.text


def get_motif_locations(protein_id, motif_matcher):
    motif_locs = []
    with tempfile.NamedTemporaryFile("w") as fp:
        fp.write(fetch_protein_fasta(protein_id))
        fp.seek(0)
        fasta = FastxFile(fp.name)
        protein_sequence = next(fasta).sequence
    matches = motif_matcher.finditer(protein_sequence)
    return [str(match.span()[0] + 1) for match in matches]


def test():
    protein_ids = ["A2Z669", "B5ZC00", "P07204_TRBM_HUMAN", "P20840_SAG1_YEAST"]
    motif_matcher = re.compile(r"(?=N[^P][ST][^P])")
    for protein_id in protein_ids:
        motif_locations = get_motif_locations(protein_id, motif_matcher)
        if motif_locations:
            print(protein_id)
            print(" ".join(motif_locations))

def main():
    with get_data_file("rosalind_mprt.txt").open() as f:
        protein_ids = [line.rstrip() for line in f.readlines()]
    motif_matcher = re.compile(r"(?=N[^P][ST][^P])")
    for protein_id in protein_ids:
        motif_locations = get_motif_locations(protein_id, motif_matcher)
        if motif_locations:
            print(protein_id)
            print(" ".join(motif_locations))


if __name__ == "__main__":
    #test()
    main()
