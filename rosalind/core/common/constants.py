import os
from os.path import dirname

DATA_DIR = os.path.join(dirname(dirname(dirname(dirname(__file__)))), 'data_sets')
RESULTS_DIR = os.path.join(dirname(dirname(dirname(dirname(__file__)))), 'results')
