from rosalind.utils import get_data_file


def reverse_complement(sequence):
    rc_lookup = dict(zip("ATGC", "TACG"))
    return "".join(rc_lookup[bp] for bp in reversed(sequence))


def test():
    input_sequence = "AAAACCCGGT"
    expected_sequence = "ACCGGGTTTT"
    assert expected_sequence == reverse_complement(input_sequence)
    print("PASS")


def main():
    with get_data_file("rosalind_revc.txt").open() as f:
        print(reverse_complement(f.readline().rstrip()))


if __name__ == "__main__":
    test()
    # main()
