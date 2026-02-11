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

suspicions_checks = {
    "external_addresses": lambda log: not (log[gloss["source_ip"]]).startswith(INTERNAL_ADDRESSES),
    "night_activity": lambda log: 0 <= int(log[gloss["timestamp"]][11:13]) < 6,
    "sensitive_ports": lambda log: log[gloss["port"]] in SENSITIVE_PORT,
    "large_ports": lambda log: int(log[gloss["size"]]) > LARGE_PACKET
}
def filter_suspicions(log):
    return filter(lambda sus: suspicions_checks[sus](log), suspicions_checks)

def filter_logs_suspicions(data):
    return map(filter_suspicions, data)

def filter_logs_with_2_suspicions(suspicions_list):
    return list(filter(lambda log_suspicions: len(log_suspicions) > 1, suspicions_list))

def gen_filter_suspect_logs(data):
    for log in data:
        if any(filter_suspicions(log)):
            yield log