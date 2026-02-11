from reader import *
from analyzer import *
from checks import *
from config import *

data = gen_load_data(DATA_PATH)
print(count_suspect_logs(data))
