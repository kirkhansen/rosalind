from pathlib import Path


def get_data_file(file_name):
    return Path(Path(__file__).parent, f"data/{file_name}")
