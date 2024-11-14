import numpy as np
import wfdb
from atriumdb import AtriumSDK

from lib.atriumdb_mariadb_sdk import sdk

FREQ_UNITS_HZ = "Hz"

class RecordHundredDigitalData:
    def __init__(self):
        self.record = wfdb.rdrecord("100", pn_dir="mitdb") #this is where we pull the record
        
        self.sig_name = self.record.sig_name[0]
        self.freq_hz = self.record.fs
        self.value_data = self.record.p_signal.T[0]

        # WFDB doesn't have time information associated with this data, so create some.
        self._period_ns = (10 ** 9) // self.record.fs
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
        device_tag = "MITDB_record_100_digital"
        new_device_id = sdk.insert_device(device_tag=device_tag)
        
        # Define a new signal.
        new_measure_id = sdk.insert_measure(measure_tag=self.sig_name, freq=self.freq_hz, freq_units=FREQ_UNITS_HZ)
        
        # EXTRA ADDED: Calculate the digital to analog scale factors.
        # Only required for digital signals to scale data??
        segment = self.record
        assert len(segment.adc_gain) == 2 and (segment.adc_gain[0] == segment.adc_gain[1]) # not sure why this is an array, just take first val
        gain = segment.adc_gain[0]
        assert len(segment.baseline) == 2 and (segment.baseline[0] == segment.baseline[1]) # not sure why this is an array, just take first val
        baseline = segment.baseline[0]
        scale_m = 1 / gain
        scale_b = -baseline / gain

        # Write Data
        sdk.write_data_easy(new_measure_id, new_device_id, self.time_data, self.value_data, self.freq_hz, 
                            freq_units=FREQ_UNITS_HZ
                            , scale_m=scale_m, scale_b=scale_b
                            )

        print("Data inserted")
        print("measure_id = ", new_measure_id)
        print("start_time_nano = ", self.start_time_nano)
        print("end_time_nano = ", self.end_time_nano)
        print("new_device_id = ", new_device_id)


RecordHundredDigitalData().insert_data(sdk)