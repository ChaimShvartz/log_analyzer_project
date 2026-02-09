from config import *
from reader import *
from analyzer import *
from reporter import get_counter_dict

def get_suspicions(data):
    external_addresses = {log for log in get_external_addresses(data)}
    night_activity = {log[gloss["source_ip"]] for log in get_night_activity(data)}
    sensitive_port = {log[gloss["source_ip"]] for log in get_sensitive_port(data)}
    large_ports = {log[gloss["source_ip"]] for log in get_unusual_size_ports(data)}
    suspicions = {
    "external_addresses": external_addresses,
    "night_activity": night_activity,
    "sensitive_ports": sensitive_port,
    "large_ports": large_ports
    }
    return {log: [sus.upper() for sus in suspicions if log in suspicions[sus]] for log in get_counter_dict(data)}

def get_addresses_with_2_suspicions(dict_suspects):
    return [pair for pair in dict_suspects.items() if len(pair[1]) > 1]