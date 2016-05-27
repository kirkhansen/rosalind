import os

from rosalind.core.common.constants import DATA_DIR, RESULTS_DIR


def get_data_file_path(rosalind_name):
    return os.path.join(DATA_DIR, 'rosalind_{}.txt'.format(rosalind_name))


def get_output_file_path(rosalind_name):
    return os.path.join(RESULTS_DIR, 'rosalind_{}.txt'.format(rosalind_name))
