from rosalind.utils import get_data_file


def findall(pattern, string):
    """
    Yields all the positions of the pattern in the string.
    """
    i = string.find(pattern)
    while i != -1:
        yield i
        i = string.find(pattern, i + 1)


def get_motif_locs(sequence, motif):
    """ Returns the location of the motif in 1-based numbering"""
    return tuple(map(lambda x: x + 1, findall(motif, sequence)))


def test():
    expected = (2, 4, 10)
    sequence = "GATATATGCATATACTT"
    motif = "ATAT"

    locations = get_motif_locs(sequence, motif)
    print(locations, expected)
    assert expected == locations
    print("PASS")


def main():
    with get_data_file("rosalind_subs.txt").open() as f:
        sequence, motif = (line.strip() for line in f.readlines())
    print(" ".join(str(index) for index in get_motif_locs(sequence, motif)))


if __name__ == "__main__":
    main()
