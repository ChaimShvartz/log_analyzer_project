import csv

DATA_PATH = 'network_traffic.log'

def load_data(data_path) -> list[list[str]] | None:
    try:
        with open(data_path) as f:
            return [line for line in csv.reader(f)]
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print(load_data(DATA_PATH))
