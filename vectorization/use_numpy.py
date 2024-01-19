from benchmark import timing_context
import numpy as np

DATA = np.random.rand(50_000_000)

with timing_context():
    mean = DATA.sum() / len(DATA)
    result = DATA - mean