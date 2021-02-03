from rosalind.utils import get_data_file


def hamming_distance(sequence0, sequence1):
    hamm_distance = 0
    for i in range(len(sequence0)):
        if sequence0[i] != sequence1[i]:
            hamm_distance += 1
    return hamm_distance



def test():
    expected = 7
    with get_data_file("rosalind_hamm.txt").open() as f:
        sequences = f.readlines()
    assert expected == hamming_distance(*sequences)
    print("PASS")


def main():
    with get_data_file("rosalind_hamm.txt").open() as f:
        sequences = f.readlines()
    print(hamming_distance(*sequences))


if __name__ == "__main__":
    #test()
    main()


