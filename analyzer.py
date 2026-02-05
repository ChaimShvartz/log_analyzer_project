from config import *

def get_external_addresses(data) -> list:
    return [line[gloss['source_ip']] for line in data if not line[gloss['source_ip']].startswith(INTERNAL_ADDRESSES)]

def get_sensitive_port(data) -> list[list]:
    return [line for line in data if line[gloss['port']] in SENSITIVE_PORT]

def get_unusual_size_ports(data) -> list:
    return [line for line in data if int(line[gloss['size']]) > PACKET_LARGE]

def tag_bigger_ports(data):
    for line in data:
        line.append("LARGE" if int(line[gloss['size']]) > PACKET_LARGE else "NORMAL")
    return data