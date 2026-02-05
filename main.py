import csv

DATA_PATH = 'network_traffic.log'
INTERNAL_ADDRESSES = ('192.168', '10')

def load_data(data_path) -> list[list[str]] | None:
    try:
        with open(data_path) as f:
            return [line for line in csv.reader(f)]
    except Exception as e:
        print(e)

def get_external_addresses(data):
    return [line[1] for line in data if not line[1].startswith(INTERNAL_ADDRESSES)]


if __name__ == '__main__':
    # print(load_data('DATA_PATH'))
    print(get_external_addresses(load_data(DATA_PATH)))
