from rosalind.utils import get_data_file


def t_to_u(sequence):
    return sequence.replace("T", "U")


def test():
    test_str = "GATGGAACTTGACTACGTAAATT"
    res = t_to_u(test_str)
    expected = "GAUGGAACUUGACUACGUAAAUU"
    assert res == expected
    print("PASS")


def main():
    with get_data_file("rosalind_rna.txt").open() as f:
        print(t_to_u(f.readline()))


if __name__ == "__main__":
    # test()
    main()
