import os

from rosalind.core.common.constants import DATA_DIR

with open(os.path.join(DATA_DIR, 'rosalind_inod.txt'), 'r') as data_file:
    data_set = data_file.readlines()
    n = int(data_set[0])

# Graph theorem, it seems, is that the number of leaves minus two equals the number of internal nodes for
# an unrooted binary tree. Checked it by drawing several graphs.

print n - 2
