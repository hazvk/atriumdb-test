# Signal data by segment

Based on (Tutorial > Methods of inserting data > Segments)[https://docs.atriumdb.io/tutorial.html#segments].

> Segments are a sequence of evenly-timed samples . A segment includes a start time, a sampling frequency, and a sequence of values. The timestamp of each value can be inferred based on the start time and the frequency.
Segments are often used for high-frequency waveforms or signals.

From root of project, run:
```
PYTHONPATH=. python src/signals_by_segment/write_data.py
PYTHONPATH=. python src/signals_by_segment/read_data.py
```