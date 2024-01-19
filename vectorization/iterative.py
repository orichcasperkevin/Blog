from benchmark import timing_context
from random import random

DATA = [random() for _ in range(50_000_000)]

with timing_context():
    mean = sum(DATA) / len(DATA)
    result = [DATA[i] - mean for i in range(len(DATA))]