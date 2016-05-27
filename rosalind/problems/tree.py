import os

from rosalind.core.common.constants import DATA_DIR


def min_number_of_edges_to_complete_tree(n, edges):
    return n - len(edges) - 1

with open(os.path.join(DATA_DIR, 'tree_test.txt'), 'r') as data_file:
    data_set = data_file.readlines()
    n = int(data_set[0])
    edges = [map(int, data_set[i].split()) for i in range(1, len(data_set))]
print min_number_of_edges_to_complete_tree(n, edges)
