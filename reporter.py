from config import *
from reader import load_data


def get_counter_dict(data):
    return {line[gloss["source_ip"]]: sum([1 if item[gloss["source_ip"]] == line[gloss["source_ip"]] else 0 for item in data]) for line in data}

def get_port_to_protocol_mapping(data):
    return {line[gloss["port"]]: line[gloss["protocol"]] for line in data}

print(get_port_to_protocol_mapping(load_data(DATA_PATH)))