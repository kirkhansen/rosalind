"""
k: number of generations to pass
n: number of children posessing Aa Bb in k-th generation
"""
from math import factorial

from rosalind.utils import get_data_file


def prob_hetero(k, n, p=0.25):
    prob = 0
    total = 2 ** k
    for gen in range(n, (total + 1)):
        prob += coeff(total, gen) * (p ** gen) * ((1 - p) ** (total - gen))
    return prob


def coeff(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def test():
    k, n = 2, 1
    print(prob_hetero(2, 1))


def main():
    with get_data_file("rosalind_lia.txt").open() as f:
        k, n = (int(x) for x in f.readline().split())
    print(prob_hetero(k, n))


if __name__ == "__main__":
    # test()
    main()
