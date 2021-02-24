from rosalind.utils import get_data_file


def probability_of_dominant_child(k, m, n):
    """
    Returns 1 - probability of getting recessive children

    using the complementary probability of getting no dominant alleles.
    The terms in the numerator correspond to the choice of the mating partners:
    1. one from the mixed and one from recessive
    2. both from mixed
    3. recessive alleles only
    """
    N = k + m + n
    return 1 - (m * n + 0.25 * m * (m - 1) + n * (n - 1)) / (N * (N - 1))


def test():
    with get_data_file("rosalind_iprb.txt").open() as f:
        k, m, n = (int(i) for i in f.readline().split())
    prob = probability_of_dominant_child(k, m, n)
    print(prob)


def main():
    with get_data_file("rosalind_iprb.txt").open() as f:
        k, m, n = (int(i) for i in f.readline().split())
    print(probability_of_dominant_child(k, m, n))


if __name__ == "__main__":
    # test()
    main()
