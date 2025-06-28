import math
from matplotlib import pyplot as plt

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))  # Add src to path

from src.lib.atriumdb_mariadb_sdk import sdk

measure_id =  2
new_device_id =  2

def graph_read_data(start_time_s = 0, end_time_s = 1805.5555555555557):
    _, read_time_data, read_value_data = sdk.get_data(measure_id=measure_id, start_time_n=start_time_s*10**9, end_time_n=end_time_s*10**9, device_id=new_device_id)
    # print(read_time_data, read_value_data)
    plt.plot(read_time_data, read_value_data)
    plt.show()

graph_read_data(end_time_s = 2)