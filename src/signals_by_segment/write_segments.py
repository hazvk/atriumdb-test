import math
import numpy as np
import wfdb
from atriumdb import AtriumSDK

from src.lib.atriumdb_mariadb_sdk import sdk

FREQ_UNITS_HZ = "Hz"
TIME_UNITS = 's'

class RecordSegmentData:
    def __init__(self):
        record = wfdb.rdrecord("100", pn_dir="mitdb", return_res=64, smooth_frames=False, m2s=False, physical=False)  # this is where we pull the record
        self.segments = record.segments if isinstance(record, wfdb.MultiRecord) else [record]

    # Remember start & end times for future query
    @property
    def start_time_nano(self) -> np.int64:
        return 0
    
    @property
    def end_time_nano(self) -> np.int64:
        return self.start_time_nano + (self._period_ns * self.value_data.size)

    def insert_data(self, sdk: AtriumSDK):
        # Define a new source.
        device_tag = "MITDB_record_100_segment"
        new_device_id = sdk.insert_device(device_tag=device_tag)

        # Iterate over the WFDB segments to extract and store signal data
        end_frame = 0
        measure_ids = []
        for segment in self.segments:
            start_frame = end_frame
            end_frame += segment.sig_len

            if segment.sig_len == 0:
                continue

            for i, signal_name in enumerate(segment.sig_name):
                freq_hz = segment.fs * segment.samps_per_frame[i]
                start_time_s = start_frame / segment.fs
                end_time_s = end_frame / segment.fs
                gain = segment.adc_gain[i]
                baseline = segment.baseline[i]
                digital_signal = segment.e_d_signal[i]

                # Define a new signal type (measure) in AtriumDB. If the signal already exists, the id will be returned
                # without defining anything new. `freq_units` must be specified!
                measure_id = sdk.insert_measure(measure_tag=signal_name, freq=freq_hz, freq_units=FREQ_UNITS_HZ)
                if measure_id not in measure_ids:
                    measure_ids.append(measure_id)

                # Scale factors such that: Analog_Signal = scale_m * Digital_Signal + scale_b
                scale_m = 1 / gain
                scale_b = -baseline / gain

                # Write the signal data to AtriumDB
                sdk.write_segment(measure_id, new_device_id, digital_signal, start_time_s, freq=freq_hz,
                    scale_m=scale_m, scale_b=scale_b, time_units=TIME_UNITS, freq_units=FREQ_UNITS_HZ)

        print("Segment inserted")
        print("measure_id = ", measure_id)
        print("start_time_s = ", 0)
        print("end_time_s = ", end_time_s)
        print("new_device_id = ", new_device_id)

RecordSegmentData().insert_data(sdk)