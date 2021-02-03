from rosalind.utils import get_data_file


def fibd(n, m):
    ages = [1] + [0] * (m - 1)
    for i in range(n - 1):
      ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)


def test():
    n, m = (6, 3)
    total_rabbit_pairs = fibd(n, m)
    assert total_rabbit_pairs == 4, total_rabbit_pairs
    print("PASS")


def main():
    with get_data_file("rosalind_fibd.txt").open() as f:
        n, m = (int(i) for i in f.readline().rstrip().split())
        print(fibd(n, m))


if __name__ == "__main__":
    #test()
    main()
