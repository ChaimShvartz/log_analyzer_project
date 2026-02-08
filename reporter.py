from config import *
from reader import load_data


def get_counter_dict(data):
    return {line[gloss["source_ip"]]: sum([1 if item[gloss["source_ip"]] == line[gloss["source_ip"]] else 0 for item in data]) for line in data}

print(get_counter_dict(load_data(DATA_PATH)))