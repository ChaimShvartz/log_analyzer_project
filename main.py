from reader import *
from analyzer import *
from checks import *
from config import *

# data = gen_load_data(DATA_PATH)
lines = gen_load_data("network_traffic.log") # generator
suspicious = gen_filter_suspect_logs(lines) # generator
detailed = gen_suspicions_list_by_log(suspicious) # generator
count = count_suspect_logs(suspicious)
print(f"Total suspicious: {count}")
