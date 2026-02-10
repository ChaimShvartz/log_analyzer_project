import csv
from config import *

def load_data(data_path) -> list[list[str]] | None:
    try:
        with open(data_path) as f:
            return [line for line in csv.reader(f)]
    except Exception as e:
        print(e)
        return []

def gen_load_data(data_path):
    try:
        with open(data_path) as f:
            for log in f:
                yield log
    except Exception:
        raise StopIteration("File not found")