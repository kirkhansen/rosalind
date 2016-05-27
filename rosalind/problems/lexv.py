from rosalind.problems.util import get_data_file_path, get_output_file_path

from itertools import product

NAME = 'lexv'

with open(get_data_file_path(NAME), 'r') as f:
    letters, max_len= f.readlines()
    # set ourselves up for success
    # allows us to use the product function with a simple if statement to get the stuff we care about
    letters = ['*'] + letters.split()
    max_len = int(max_len)

lexv = []
for item in product(letters, repeat=max_len):
    # Include all items without *'s.
    if '*' not in item:
        lexv.append(''.join(item))
    else:
        # Items with only trailing *'s should also be included with the *'s removed.
        for i in range(1, max_len):
            if ''.join(item[i:max_len]) == '*' * (max_len - i) and '*' not in item[:i]:
                lexv.append(''.join(item).replace('*', ''))

with open(get_output_file_path(NAME), 'w') as outfile:
    outfile.write('\n'.join(lexv))
