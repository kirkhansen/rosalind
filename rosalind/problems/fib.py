from rosalind.utils import get_data_file


def fib(n, k):
    f1, f2 = 1, 1
    n = int(n)
    k = int(k)
    for i in range(2, n):
        f1, f2 = f2, k * f1 + f2
    return f2


def test():
    n, num_rabbit_pairs = 5, 3
    total_rabbit_pairs = fib(5, 3)
    assert total_rabbit_pairs == 19, total_rabbit_pairs
    print("PASS")


def main():
    with get_data_file("rosalind_fib.txt").open() as f:
        n, num_rabbit_pairs = f.readline().rstrip().split()
        print(fib(n, num_rabbit_pairs))


if __name__ == "__main__":
    # test()
    main()
