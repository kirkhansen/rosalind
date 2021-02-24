from itertools import permutations

from rosalind.utils import get_data_file


def perm(n):
    perms = list(permutations(range(1, n + 1)))
    print(len(perms))
    for p in perms:
        print(" ".join(str(i) for i in p))
    return perms


def test():
    perm(3)


def main():
    with get_data_file("rosalind_perm.txt").open() as f:
        num_perms = int(f.readline().rstrip())
    perms = perm(num_perms)
    with get_data_file("rosalind_perm_out.txt").open("w") as f:
        f.write(str(len(perms)) + "\n")
        for p in perms:
            f.write(" ".join(str(i) for i in p) + "\n")


if __name__ == "__main__":
    # test()
    main()
