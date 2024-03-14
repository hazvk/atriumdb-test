import numpy as np
import wfdb
from atriumdb import AtriumSDK

from lib.atriumdb_mariadb_sdk import sdk

FREQ_UNITS_HZ = "Hz"

class RecordHundredData:
    def __init__(self):
        record = wfdb.rdrecord("100", pn_dir="mitdb") #this is where we pull the record
        
        self.sig_name = record.sig_name[0]
        self.freq_hz = record.fs
        self.value_data = record.p_signal.T[0]

        # WFDB doesn't have time information associated with this data, so create some.
        self._period_ns = (10 ** 9) // record.fs
        self.time_data = np.arange(self.value_data.size, dtype=np.int64) * self._period_ns

    # Remember start & end times for future query
    @property
    def start_time_nano(self) -> np.int64:
        return 0
    
    @property
    def end_time_nano(self) -> np.int64:
        return self.start_time_nano + (self._period_ns * self.value_data.size)

    def insert_data(self, sdk: AtriumSDK):
        # Define a new source.
        device_tag = "MITDB_record_100"
        new_device_id = sdk.insert_device(device_tag=device_tag)
        
        # Define a new signal.
        new_measure_id = sdk.insert_measure(measure_tag=self.sig_name, freq=self.freq_hz, freq_units=FREQ_UNITS_HZ)

        # Write Data
        sdk.write_data_easy(new_measure_id, new_device_id, self.time_data, self.value_data, self.freq_hz, freq_units=FREQ_UNITS_HZ)

        print("Data inserted")
        print("measure_id = ", new_measure_id)
        print("start_time_nano = ", self.start_time_nano)
        print("end_time_nano = ", self.end_time_nano)
        print("new_device_id = ", new_device_id)


RecordHundredData().insert_data(sdk)