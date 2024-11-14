from matplotlib import pyplot as plt

from lib.atriumdb_mariadb_sdk import sdk

measure_id =  1
new_device_id =  1

def graph_read_data(start_time_nano = 0, end_time_nano = 1_805_555_050_000):
    _, read_time_data, read_value_data = sdk.get_data(measure_id=measure_id, start_time_n=start_time_nano, end_time_n=end_time_nano, device_id=new_device_id)
    # print(read_time_data, read_value_data)
    plt.plot(read_time_data, read_value_data)
    plt.show()

graph_read_data(end_time_nano=2 * 10**9)