"""
Input will be 6 nums where each num represents
the number of couples exhibiting the following
genotytes:
    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa
"""
from rosalind.utils import get_data_file


PROB_DOM_LOOKUP = [1, 1, 1, .75, .50, 0]


def get_expected_doms(population, num_children=2):
    return sum(num_couples * num_children * PROB_DOM_LOOKUP[i]
            for i, num_couples in enumerate(population)
    )


def test():
    population = [int(x) for x in "1 0 0 1 0 1".split()]
    expected = 3.5
    res = get_expected_doms(population)
    assert expected == res, res
    print("PASS")


def main():
    with get_data_file("rosalind_iev.txt").open() as f:
        population = [int(x) for x in f.readline().split()]
        print(get_expected_doms(population))


if __name__ == "__main__":
    #test()
    main()
