from config import *
from reader import load_data


def get_counter_dict(data):
    return {line[gloss["source_ip"]]: sum([1 if item[gloss["source_ip"]] == line[gloss["source_ip"]] else 0 for item in data]) for line in data}

def get_port_to_protocol_mapping(data):
    return {line[gloss["port"]]: line[gloss["protocol"]] for line in data}

def get_time(data):
    times = map(lambda log: log[gloss["timestamp"]][11:13], data)
    return list(map(lambda time: time if time[0] != '0' else time[1], times))

def convert_bytes_to_KB(sizes):
    return list(map(lambda size: size / 1024, sizes))
