from pprint import pprint

from pysam import FastaFile

from rosalind.utils import get_data_file


def build_overlap_graph(fasta, overlap=3):
    """
    Args:
        fasta: fasta object of sequences
        overlap: number of base pairs to overlap with
    """
    graph = []
    for reference in fasta.references:
        seq1 = fasta.fetch(reference)
        for next_reference in fasta.references:
            seq2 = fasta.fetch(next_reference)
            if reference == next_reference:
                continue
            if seq1[-overlap:] == seq2[:overlap]:
                graph.append((reference, next_reference))
    return graph


def print_graph(graph):
    for edge in graph:
        print(f"{edge[0]} {edge[1]}")


def test():
    fasta = FastaFile(get_data_file("rosalind_grph_test.txt"))
    expected = [
        ("Rosalind_0498", "Rosalind_2391"),
        ("Rosalind_0498", "Rosalind_0442"),
        ("Rosalind_2391", "Rosalind_2323"),
    ]
    graph = build_overlap_graph(fasta)
    assert expected == graph
    print("PASS")


def main():
    fasta = FastaFile(get_data_file("rosalind_grph.txt"))
    print_graph(build_overlap_graph(fasta))


if __name__ == "__main__":
    # test()
    main()
